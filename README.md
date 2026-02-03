# Teste Técnico Power Data - Star Wars API

## 📋 Sobre o Projeto

Este projeto é uma **API RESTful** desenvolvida em Python utilizando FastAPI que atua como um wrapper da [SWAPI (Star Wars API)](https://swapi.dev). A aplicação fornece endpoints organizados para consultar informações sobre o universo Star Wars, incluindo personagens, filmes, planetas e naves espaciais.

### 🎯 Propósito

Criado como teste técnico para a Power Data, este projeto demonstra:
- Desenvolvimento de APIs REST com FastAPI
- Integração com APIs externas
- Organização de código em rotas e serviços
- Boas práticas de desenvolvimento Python

## 🚀 Tecnologias Utilizadas

- **Python 3.13+**
- **FastAPI 0.128.0** - Framework web moderno e rápido para construção de APIs
- **Uvicorn 0.40.0** - Servidor ASGI para executar a aplicação
- **Requests 2.32.5** - Biblioteca HTTP para chamadas à API externa
- **Pydantic** - Validação de dados (via FastAPI)

## 📁 Estrutura do Projeto

```
Teste-Tecnico-Power-Data/
├── app/
│   ├── main.py                 # Configuração principal da aplicação FastAPI
│   ├── routes/                 # Definição dos endpoints da API
│   │   ├── people.py          # Rotas relacionadas a personagens
│   │   ├── films.py           # Rotas relacionadas a filmes
│   │   ├── planets.py         # Rotas relacionadas a planetas
│   │   └── starships.py       # Rotas relacionadas a naves espaciais
│   └── services/
│       └── swapi_service.py   # Serviço para chamadas à SWAPI
├── pyproject.toml              # Metadados e dependências do projeto
├── requirements.txt            # Pacotes instalados
└── README.md                   # Documentação do projeto
```

## 🔧 Instalação e Configuração

### Pré-requisitos

- Python 3.13 ou superior
- pip ou uv (gerenciador de pacotes)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/MarivaldoDev/Teste-Tecnico-Power-Data.git
cd Teste-Tecnico-Power-Data
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

Ou usando uv:
```bash
uv sync
```

3. Execute a aplicação:
```bash
uvicorn app.main:app --reload
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

### Documentação Interativa

Após iniciar a aplicação, acesse:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Endpoints Disponíveis

#### 🏠 Health Check
- `GET /` - Verifica o status da API

#### 👥 People (Personagens)
- `GET /people` - Lista todos os personagens
  - Query params: `name`, `gender`
- `GET /people/{id}/films` - Retorna os filmes em que o personagem apareceu
- `GET /people/{id}/planet` - Retorna o planeta natal do personagem
- `GET /people/{id}/starships` - Retorna as naves pilotadas pelo personagem

#### 🎬 Films (Filmes)
- `GET /films` - Lista todos os filmes
  - Query params: `title`, `director`
- `GET /films/{id}/characters` - Retorna todos os personagens de um filme

#### 🌍 Planets (Planetas)
- `GET /planets/{id}/residents` - Retorna os residentes de um planeta

#### 🚀 Starships (Naves Espaciais)
- `GET /starships/{id}/pilots` - Retorna os pilotos de uma nave espacial

## 💡 Exemplos de Uso

### Listar todos os personagens
```bash
curl http://localhost:8000/people
```

### Buscar personagens por nome
```bash
curl http://localhost:8000/people?name=Luke
```

### Obter filmes de um personagem específico
```bash
curl http://localhost:8000/people/1/films
```

### Listar filmes por diretor
```bash
curl http://localhost:8000/films?director=George%20Lucas
```

## 🌐 Fonte de Dados

Todos os dados são obtidos da **SWAPI (Star Wars API)** - uma API pública e gratuita que contém informações abrangentes sobre o universo Star Wars.

- URL Base: `https://swapi.dev/api`
- Documentação: [swapi.dev](https://swapi.dev)

## 🎨 Funcionalidades

1. **Listagem com Filtros**: Filtre personagens por nome/gênero e filmes por título/diretor
2. **Navegação Relacional**: Acesse facilmente informações relacionadas (ex: filmes de um personagem, personagens de um filme)
3. **Informações Detalhadas**: Consulte planetas natais, naves pilotadas, residentes de planetas, etc.
4. **Documentação Automática**: Swagger UI e ReDoc gerados automaticamente pelo FastAPI

## 📝 Status do Projeto

✅ API funcional com endpoints principais implementados  
✅ Integração com SWAPI completa  
✅ Documentação automática disponível  
🔄 Em desenvolvimento contínuo

## 👨‍💻 Autor

Marivaldo

## 📄 Licença

Este projeto foi desenvolvido como teste técnico para a Power Data.
 
## ☁️ Deploy no GCP (Cloud Run)

Recomendo usar **Cloud Run** para este projeto (suporta ASGI/FastAPI sem adaptação). Para facilitar o deploy incluí um `Dockerfile` e o script `deploy.sh`.

Passos rápidos:

```bash
# Edite a variável PROJECT abaixo ou exporte antes de rodar:
export PROJECT=your-gcp-project-id
./deploy.sh
```

O script faz `gcloud builds submit` e deploya no Cloud Run. Se preferir Cloud Functions + API Gateway, eu posso adicionar um wrapper (Functions Framework) e o OpenAPI para o Gateway.