# Área de testes

Área de experimentações e testes. Nada mais (por enquanto).

## Para Gitpod

Como boa prática, o _chatbot_ usa o _token_ do Discord da variável de ambiente (carregada pelo módulo `python-dotenv`) a ser definida na [interface Web](https://gitpod.io/variables):

- Name: `DISCORD_TOKEN`
- Value: `<token>`
- Scope: `*/*` (o ideal é reduzir o escopo para a organização/usuário e repositório - no meu caso, `boidacarapreta/adcipt20222`)

Além disso, o arquivo `.gitpod.yml` automatiza a instalação das dependências. Assim, todo novo _pod_ criado estará com o ambiente pronto para uso.

## Para VSCode

Recomenda-se o uso de ambiente virtual:

```sh
# Criar o ambiente virtual (na família Debian é preciso o pacote python3-env)
python3 -m venv venv

# Carregar o ambiente virtual
source venv/bin/activate

# Atualizar o pip (por garantia)
pip install --upgrade pip 

# Uma vez dentro do ambiente virtual, instalar as dependências
pip install -r requirements.txt 
```

Sobre o _token_, foi seguida a documentação do módulo `python-dotenv`, onde o arquivo `.env` (devidamente listado em `.gitignore`) armazena o seu valor:

```
DISCORD_TOKEN=<token>
```

## Para todas as IDEs baseadas em VSCode (incluindo Gitpod)

O arquivo `.vscode/launch.json` tem uma entrada para o arquivo `chatbot.py` para execução e depuração.
