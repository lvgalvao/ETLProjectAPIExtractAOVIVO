import logging
import azure.functions as func
from azure.keyvault.secrets import SecretClient
import requests
from datetime import datetime
import pyodbc
from azure.identity import DefaultAzureCredential


app = func.FunctionApp()

def extrair_dados_bitcoin():
    """Extrai o JSON completo da API da Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        logging.error(f"Erro na API: {resposta.status_code}")
        return None

def tratar_dados_bitcoin(dados_json):
    """Transforma os dados brutos da API e adiciona timestamp."""
    valor = float(dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    timestamp = datetime.now()
    
    dados_tratados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }
    return dados_tratados

def salvar_dados_sqlserver(dados):
    """Salva os dados no banco SQL Server."""
    try:
        # Obter URL do Key Vault e credenciais
        key_vault_url = "https://minhasenhas.vault.azure.net/"
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=key_vault_url, credential=credential)
        sqlusername = client.get_secret("sqlusername")
        sqlpassword = client.get_secret("sqlpassword")
        print(sqlusername)
        print(sqlpassword)
        # Conexão com o banco de dados
        server = "workshopazuredatavase.database.windows.net"
        database = "meubancodedadosaovivo "
        driver = "{ODBC Driver 18 for SQL Server}"

        cnxn = pyodbc.connect(
            f"DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={sqlusername.value};PWD={sqlpassword.value}"
        )

        insert_query = """
        INSERT INTO BitcoinData (valor, criptomoeda, moeda, timestamp)
        VALUES (?, ?, ?, ?)
        """

        with cnxn.cursor() as cursor:
            cursor.execute(
                insert_query,
                dados["valor"],
                dados["criptomoeda"],
                dados["moeda"],
                dados["timestamp"],
            )
            cnxn.commit()
            logging.info(f"[{dados['timestamp']}] Dados salvos no SQL Server!")

    except pyodbc.Error as ex:
        logging.error(f"Erro ao inserir dados no SQL Server: {ex}")


@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False)
def timer_trigger_generate_number(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.warning('A execução do timer está atrasada!')

    # Extrai os dados da API
    dados_brutos = extrair_dados_bitcoin()
    if dados_brutos:
        # Transforma os dados extraídos
        dados_tratados = tratar_dados_bitcoin(dados_brutos)
        
        # Registra os dados tratados nos logs
        logging.info(f"Dados do Bitcoin: {dados_tratados}")

        salvar_dados_sqlserver(dados_tratados)

        logging.info(f"Dados salvos no Banco")
    else:
        logging.error("Falha ao processar os dados do Bitcoin.")