# ADC/IPT 2022.2

Para este semestre de 2022.2, nas disciplinas de Administração de Redes de Computadores (ADC) e Telefonia IP (IPT), foi adotado um único projeto prático, integrado. Por decisão da turma, foi desenvolvido um _chatbot_ com suporte a texto e áudio para Discord.

O registro do acompanhamento do projeto foi feito com [kanban](https://github.com/users/boidacarapreta/projects/2/views/1) e [_milestones_](https://github.com/users/boidacarapreta/projects/2/views/2).

## Como rodar o jogo

Este bot foi projetado com a biblioteca `discord.py`, sem _framework_ como [errbot](https://errbot.readthedocs.io/) ou [opsdroid](https://opsdroid.dev), para rodar no Discord. Assim, convém ver a sua [documentação para criar o bot e integrar a um servidor](https://discordpy.readthedocs.io/en/stable/#getting-started). A persistência dos dados foi feita via MongoDB. Neste semestre, adotamos o [MongoDB Cloud Atlas](https://cloud.mongodb.com), conforme [#14](https://github.com/boidacarapreta/adcipt20222/issues/14), mas pode ser usada uma solução local.

### No Gitpod

Como [boa prática](https://12factor.net/pt_br/), o _chatbot_ usa o _token_ do Discord da variável de ambiente (carregada pelo módulo `python-dotenv`) definida na [interface Web](https://gitpod.io/variables):

- Name: `DISCORD_TOKEN`
- Value: `<token>`
- Scope: `*/*` (o ideal é reduzir o escopo para a organização/usuário e repositório - no meu caso, `boidacarapreta/adcipt20222`)

Além disso, o arquivo `.gitpod.yml` automatiza a instalação das dependências. Assim, todo novo _pod_ criado estará com o ambiente pronto para uso.

Em relação ao MongoDB, devem ser criados mais 3 variáveis de ambiente:

- `MONGODB_USERNAME`: usuário com acesso de leitura e escrita a base de dados;
- `MONGODB_PASSWORD`: senha associada ao usuário;
- `MONGODB_CLUSTER`: endereço (FQDN) do servidor ou _cluster_ (Cloud Atlas).

### No VSCode

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

Sobre as variáveis de ambiente, foi seguida a documentação do módulo `python-dotenv`, onde o arquivo `.env` (devidamente listado em `.gitignore`) armazena o seu valor:

```
DISCORD_TOKEN=<token>
MONGODB_USERNAME=<usuário>
MONGODB_PASSWORD=<senha>
MONGODB_CLUSTER=<FQDN>
```

### Em todas as IDEs baseadas em VSCode (incluindo aquelas _online_)

O arquivo `.vscode/launch.json` tem uma entrada para o arquivo `chatbot.py` para execução e depuração.
