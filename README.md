# Área de testes

Área de experimentações e testes. Nada mais (por enquanto).

## Sobre o jogo

(Ainda é uma ideia bastante crua...)

Jogos baseados em texto sofrem, no meu entendimento particular, de um problema de ritmo: após o conhecimento das regras do jogo, é possível que o jogo rapidamente fique repetitivo e mecânico. [Na primeira vez em que pensei em um jogo de escapatória de um labirinto](https://github.com/boidacarapreta/arc20211) isso ficou claro: a repetição de comandos para atingir um objetivo. Por que não usar comandos mais complexos (`caminhar até encontrar uma porta` ao invés de `andar para frente`) para tornar a interação mais fluida - ou natural. Aliás, é pensando dessa forma que percebo como [os clássicos](https://en.wikipedia.org/wiki/Colossal_Cave_Adventure) já sabiam disso há 40, 50 anos (e por isso ressoam até hoje).

(Bom, vamos lá...)

O jogo é basicamente um *roguelike*: escapar de um labirinto, ou masmorra, de dimensões de 10x10x10 blocos. Claro, tudo gerado proceduralmente: portas, escadas, objetos dispostos (baús, armas) e, claro, inimigos. Alguma inspiração do filme [Cubo](https://en.wikipedia.org/wiki/Cube_(1997_film)), porém com o labirinto fixo por toda a partida. Outra inspiração será a _cena_ da praia de [Neuromancer](https://en.wikipedia.org/wiki/Neuromancer), o que também lembra várias cenas de experimentos de [Matrix](https://en.wikipedia.org/wiki/The_Matrix) - como aquela de saltar sobre os prédios. Enfim, é ver até onde vai a toca do coelho...

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
