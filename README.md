# Star Wars API – Teste Técnico Power Data

API REST desenvolvida como parte de um teste técnico, utilizando **FastAPI**, com integração à **SWAPI (Star Wars API)**.  
O objetivo do projeto é expor endpoints que permitem consultar e correlacionar dados do universo Star Wars, aplicando boas práticas de backend, testes automatizados e conceitos de arquitetura em nuvem.


## 🚀 Tecnologias Utilizadas

- Python 3.11
- FastAPI
- Requests
- Pydantic
- Pytest
- Coverage
- Docker



## 📁 Estrutura do Projeto


```bash
app/
├── core/
│ ├── logging.py # Configuração centralizada de logs
│ └── security.py # Autenticação via API Key
├── routes/ # Rotas da aplicação
├── services/ # Integração com a SWAPI
├── schemas/ # Schemas Pydantic (contratos de resposta)
├── main.py # Inicialização da aplicação
tests/
├── test_routes.py
├── test_services.py
├── test_security.py
Dockerfile
requirements.txt
.env.example
```

## Autenticação

Defina a variável de ambiente `API_KEY` no arquivo `.env`.

Exemplo:

API_KEY="powerofdata-key"

Em seguida, envie o header:

X-API-Key: powerofdata-key


Essa abordagem garante separação entre código e dados sensíveis, sendo adequada tanto para ambientes locais quanto cloud.


## Pydantic

O **Pydantic** foi utilizado de forma **pontual e estratégica**, principalmente para:

- Definir contratos de resposta
- Garantir validação automática dos dados
- Melhorar a documentação gerada pelo Swagger

O objetivo foi demonstrar domínio da ferramenta sem acoplar a aplicação à estrutura completa da API externa (SWAPI).


## Logs

O projeto possui **logging centralizado**, aplicado principalmente:

- Nas chamadas à SWAPI
- Em pontos críticos de execução das rotas

Os logs são compatíveis com ambientes cloud (como GCP), sendo automaticamente capturados por ferramentas como **Cloud Logging**.


## Testes Automatizados

Os testes foram desenvolvidos utilizando **Pytest**, cobrindo:

- Rotas da API
- Autenticação por API Key
- Serviços de integração com a SWAPI
- Cenários de erro e respostas inválidas

### Executar os testes

```bash
pytest
```

### Gerar relatório de cobertura
```bash
coverage run -m pytest
coverage report
coverage html
```

## Docker
A aplicação pode ser executada em ambiente containerizado.

### Build da imagem
```bash
docker build -t starwars-api .
```

### Executar o container
```bash
docker run -p 8000:8000 --env-file .env starwars-api
```

Acesse a documentação interativa:
```bash
http://localhost:8000/docs
```

## ☁️ Deploy na Google Cloud Platform (GCP)

A aplicação foi projetada para ser executada em ambiente serverless na GCP.

### Arquitetura sugerida

- Cloud Functions: execução da API FastAPI
- API Gateway: exposição e gerenciamento dos endpoints
- Cloud Logging: observabilidade e monitoramento
- Variáveis de ambiente: gerenciamento seguro da API Key

### Fluxo da aplicação
```bash
Cliente → API Gateway → Cloud Function → SWAPI
```
O projeto está preparado para esse cenário sem necessidade de alterações significativas no código.


## Observações Finais

O foco do projeto é demonstrar boas práticas de backend, organização de código, testes automatizados e visão de arquitetura em nuvem.

Foram evitadas soluções complexas ou overengineering, mantendo o escopo alinhado ao desafio proposto.


## 👨‍💻 Autor

Desenvolvido por Marivaldo Pedro