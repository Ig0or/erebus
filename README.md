## Erebus

### SOBRE O PROJETO :file_folder:
Microsserviço em Python utilizando mensageria com Kafka com o objetivo de praticar processos assíncronos envolvendo filas.

O Erebus é um serviço que processa as ordens que estão no tópico do Kafka e que foram enviadas pela Nyx (https://github.com/Ig0or/nyx).

<hr>

### TECNOLOGIAS QUE ESTÃO SENDO USADAS :space_invader:

:small_blue_diamond: Cryptography: Descriptografar os valores que foram enviados para o tópico do Kafka.

:small_blue_diamond: Kafka-python: Client do Kafka para conexão e recebimento das mensagens.

:small_blue_diamond: Loglifos: Loggar avisos/erros.

:small_blue_diamond: Pip-chill: Alternativa ao pip-freeze, agrupando somente top-level.

:small_blue_diamond: Pyfiglet: Prints mais bonitinhos :P

:small_blue_diamond: Pymongo: Conexão com banco de dados MongoDB.

:small_blue_diamond: Python-decouple: Utilizar variaveis de ambiente.

:small_blue_diamond: Requests: Realizar requests para uma API externa com informações das ordens recebidas.

<hr>

### PARA EXECUTAR O SERVIDOR VIA DOCKER COMPOSE :floppy_disk:
- Com o Docker e Docker Compose instalados na sua maquina rode o comando ```docker-compose up -d``` ou ```docker compose up -d``` na pasta raiz do projeto.
- Ao executar com o Docker, será criado uma imagem para o Kafka, MongoDB, Nyx (produtor dos dados) e o Erebus (consumidor do dados)
- Acesse ```localhost:8080/docs```


### PARA EXECUTAR O PROCESSO SEM O DOCKER :calling:
- Crie um novo ambiente virtual com ```python3 -m virtualenv .venv``` ou ```python3 -m venv .venv```
- Ative o seu novo ambiente virtual com ```source ./venv/bin/activate``` ou ```.venv\Scripts\activate.bat```
- Instale as dependências do projeto com ```pip install -r requirements.txt```

- Crie um arquivo ```.env``` na raiz do projeto de acordo com o ```.env_exemple```

```
-- KAFKA --
KAFKA_URI= Host de conexão com o Kafka.
KAFKA_CLIENT_ID= Nome do client que está usando o Kafka.
KAFKA_GROUP_ID= Nome do consumidor.
KAFKA_TOPIC_NAME= Nome do tópico de onde as mensagens serão consumidas.

-- MONGODB --
MONGO_HOST= Conexão com o MongoDB.
MONGO_DATABASE= Nome do database.
MONGO_COLLECTION= Nome da collection.

-- DEOBFUSCATE --
FERNET_KEY= Chave que será utilizada para descriptografar os valores enviados para o Kafka - Com a venv ativada execute o comando "python3 generate_fernet_key_script.py" para gerar uma nova chave.
```

- Execute o comando ```python3 erebus.py``` para startar o processo.
