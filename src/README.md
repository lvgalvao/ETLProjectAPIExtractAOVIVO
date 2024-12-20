# Meu Projeto Docker

## 🏃‍♂️ Passos para Rodar o Projeto

### 1. Clonar o Repositório

```bash
git clone git@github.com:lvgalvao/ETLProjectAPIExtractAOVIVO.git
```

### 2. Navegar para o Diretório `src`

```bash
cd ETLProjectAPIExtractAOVIVO/src
```

### 3. Criar a Imagem Docker

```bash
docker build -t etl_api:latest .
```

### 4. Criar e Configurar o Arquivo `.env`

```bash
cp .env-exemplo .env

cat <<EOL > .env
OPENAI_API_KEY=<sua_key>
POSTGRES_USER=<sua_key>
POSTGRES_PASSWORD=<sua_key>
POSTGRES_HOST=<sua_key>
POSTGRES_PORT=<sua_key>
POSTGRES_DB=<sua_key>
LOGFIRE_TOKEN=<sua_key>
EOL
```

### 5. Rodar a Aplicação com Docker Compose

```bash
docker-compose up -d
```

---

## 📌 Notas Adicionais

- **Certifique-se de que o Docker e o Docker Compose estejam instalados** na sua máquina ou na Azure VM antes de executar os comandos acima.
  
- **Mantenha o arquivo `.env` seguro** e evite versioná-lo em repositórios públicos para proteger suas credenciais e chaves de API.

- **Verifique os containers em execução** usando:

  ```bash
  docker-compose ps
  ```

- **Para visualizar os logs da aplicação**:

  ```bash
  docker-compose logs -f
  ```

- **Para parar a aplicação**:

  ```bash
  docker-compose down
  ```

---


## 📚 Recursos Úteis

- [Documentação do Docker](https://docs.docker.com/)
- [Documentação do Docker Compose](https://docs.docker.com/compose/)
- [Melhores Práticas para Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)