Aqui está um exemplo de README para o seu arquivo `exemplo_05.py`, incluindo instruções de instalação e uma explicação sobre o que o código faz.

# Exemplo 05 - Uso da API OpenAI

Este exemplo demonstra como fazer uma chamada à API OpenAI para obter uma resposta a uma pergunta específica. O código utiliza a biblioteca `requests` para enviar uma solicitação HTTP e a biblioteca `dotenv` para gerenciar variáveis de ambiente.

## Pré-requisitos

Antes de executar o código, você precisa ter o Python instalado em sua máquina. Além disso, você deve ter uma chave de API da OpenAI. 

## Instalação

1. Clone este repositório ou baixe o arquivo `exemplo_05.py`.
2. Crie um arquivo chamado `requirements.txt` e adicione as seguintes dependências:

```
requests
python-dotenv
```

3. Instale as dependências usando o pip:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na mesma pasta que o seu script e adicione sua chave de API da OpenAI:

```
OPENAI_API_KEY=sua_chave_api_aqui
```

## Execução

Para executar o exemplo, use o seguinte comando no terminal:

```bash
python exemplos/exemplo_05.py
```

## O que o código faz

- O código carrega as variáveis de ambiente do arquivo `.env`.
- Define a URL da API OpenAI e os cabeçalhos necessários para a solicitação.
- Cria um objeto de dados que contém o modelo a ser usado e a mensagem do usuário.
- Envia uma solicitação POST para a API e imprime a resposta recebida, que contém a resposta à pergunta "Qual é a capital da França?".

## Observações

Certifique-se de que sua chave de API está correta e que você tem acesso à API OpenAI.

Sinta-se à vontade para ajustar qualquer parte do README conforme necessário!
