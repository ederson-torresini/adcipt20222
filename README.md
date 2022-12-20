# ADC/IPT 2022.2

Para este semestre de 2022.2, nas disciplinas de Administração de Redes de Computadores (ADC) e Telefonia IP (IPT), será adotado um único projeto prático, integrado. Por decisão da turma, será desenvolvido um _chatbot_ com suporte a texto e áudio para Discord.

Para acompanhamento do projeto: [kanban](https://github.com/users/boidacarapreta/projects/2/views/1) e [_milestones_](https://github.com/users/boidacarapreta/projects/2/views/2).

## Como rodar o jogo

### No Gitpod

Como boa prática, o _chatbot_ usa o _token_ do Discord da variável de ambiente (carregada pelo módulo `python-dotenv`) a ser definida na [interface Web](https://gitpod.io/variables):

- Name: `DISCORD_TOKEN`
- Value: `<token>`
- Scope: `*/*` (o ideal é reduzir o escopo para a organização/usuário e repositório - no meu caso, `boidacarapreta/adcipt20222`)

Além disso, o arquivo `.gitpod.yml` automatiza a instalação das dependências. Assim, todo novo _pod_ criado estará com o ambiente pronto para uso.

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

Sobre o _token_, foi seguida a documentação do módulo `python-dotenv`, onde o arquivo `.env` (devidamente listado em `.gitignore`) armazena o seu valor:

```
DISCORD_TOKEN=<token>
```

### Em todas as IDEs baseadas em VSCode (incluindo aquelas _online_)

O arquivo `.vscode/launch.json` tem uma entrada para o arquivo `chatbot.py` para execução e depuração.

## Equipes

| Equipe                                                     | Projeto                                                            | Repositório                                                             | E1  | E2  | E3  | E4  | E5  | E6  | E7  | E8  |
| ---------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| [AK e MC](https://github.com/AK-MC)                        | [🔗](https://github.com/orgs/AK-MC/projects/1/views/1)             | [Kayla's Adventure](https://github.com/AK-MC/Kayla-s-adventure)         | 6   | 6   | 6   | 6   | 6   | 6   | 6   | 6   |
| [aifbot](https://github.com/aifbot)                        | [🔗](https://github.com/orgs/aifbot/projects/1)                    | [discord-chabot](https://github.com/aifbot/discord-chatbot)             | 6   | 8   | 8   | 6   | 6   | 6   | 6   | 6   |
| [Amongus Inc.](https://github.com/Amongus-Inc)             | [🔗](https://github.com/orgs/Amongus-Inc/projects/2/views/1)       | [Reigns IFSC](https://github.com/Amongus-Inc/ReignsIFSC)                | 6   | 6   | 6   | 6   | 6   | 6   | 6   | 6   |
| [Augusto e Willian](https://github.com/Augusto-e-Willian)  | [🔗](https://github.com/orgs/Augusto-e-Willian/projects/1/views/1) | [chatbot](https://github.com/Augusto-e-Willian/chatbot)                 | 6   | 6   | 6   | 6   | 6   | 6   | 6   | 6   |
| [Enzo e Davi](https://github.com/enzo-davi)                | [🔗](https://github.com/orgs/enzo-davi/projects/1/views/1)         | [my game](https://github.com/enzo-davi/my-game)                         | 6   | 6   | 6   | 6   | 6   | 6   | 6   | 6   |
| [Higor com H](https://github.com/higor-com-h)              | [🔗](https://github.com/orgs/higor-com-h/projects/1)               | [Jogo sem nome](https://github.com/higor-com-h/jogosemnome)             | 6   | 6   | 0   | 0   | 0   | 0   | 0   | 0   |
| [Igor e Guilherme](https://github.com/igor-e-gui)          | [🔗](https://github.com/orgs/igor-e-gui/projects/1)                | [Cuidado onde pisa](https://github.com/igor-e-gui/cuidado-onde-pisa)    | 6   | 6   | 6   | 6   | 6   | 6   | 6   | 6   |
| [Nico e Juca](https://github.com/NicoJuca-Desenvolvimento) | [🔗](https://github.com/orgs/NicoJuca-Desenvolvimento/projects/1)  | [Minecraft](https://github.com/NicoJuca-Desenvolvimento/Minecraft)      | 6   | 6   | 6   | 6   | 6   | 6   | 6   | 6   |
| [Re-Red](https://github.com/RE-RED)                        | [🔗](https://github.com/orgs/RE-RED/projects/4)                    | [clooli](https://github.com/RE-RED/clooli)                              | 6   | 6   | 6   | 6   | 6   | 6   | 6   | 0   |
| [Super Poderosas](https://github.com/super-poderosas)      | [🔗](https://github.com/orgs/super-poderosas/projects/2)           | [Caixa de memórias](https://github.com/super-poderosas/caixadememorias) | 6   | 6   | 6   | 6   | 6   | 6   | 6   | 0   |
| [Os Vieiras](https://github.com/OsVieiras)                 | [🔗](https://github.com/orgs/OsVieiras/projects/2)                 | [Chatbot Bina](https://github.com/OsVieiras/Chatbot-Bina)               | 6   | 6   | 6   | 6   | 6   | 6   | 6   | 6   |
| [ThuzyFS](https://github.com/ThuzyFS)                      | -                                                                  | [Chat-Bot](https://github.com/ThuzyFS/Chat-Bot)                         | 6   | 6   | 6   | 6   | 6   | 6   | 6   | 6   |
