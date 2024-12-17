
# ETLProjectAPIExtractAOVIVO

## Descrição do Projeto
Este projeto é uma implementação de um processo ETL (Extração, Transformação e Carga) utilizando Python e a biblioteca `requests` para extrair dados de uma API. O objetivo é coletar dados em tempo real, transformá-los conforme necessário e carregá-los em um banco de dados ou arquivo para análise posterior.

## Tecnologias Utilizadas
- Python
- requests
- pandas (opcional, para manipulação de dados)
- SQLAlchemy (opcional, para interação com bancos de dados)

## Estrutura do Projeto
```
ETLProjectAPIExtractAOVIVO/
│
├── src/
│   ├── extract.py      # Script para extração de dados da API
│   ├── transform.py    # Script para transformação dos dados
│   └── load.py         # Script para carga dos dados
│
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```

## Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/ETLProjectAPIExtractAOVIVO.git
   cd ETLProjectAPIExtractAOVIVO
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o processo ETL:
   ```bash
   python src/extract.py
   python src/transform.py
   python src/load.py
   ```

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
