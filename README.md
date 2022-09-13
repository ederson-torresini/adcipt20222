# ADC/IPT 2022.2

Para este semestre de 2022.2, nas disciplinas de Administração de Redes de Computadores (ADC) e Telefonia IP (IPT), será adotado um único projeto prático, integrado. Por decisão da turma, será desenvolvido um _chatbot_ com suporte a texto e áudio para Discord.

Para auxiliar na metodologia de ensino, baseada em projeto, será criado um projeto modelo, de minha livre escolha. Pensei o seguinte: se há [experimentos com jogos em semestres anteriores](https://boidacarapreta.gitbook.io/projetos/integrado-ao-ensino-medio-em-telecomunicacoes/aplicacao-web-com-javascript), por que não aproveitar a história desenvolvida até então?

Durante a pandemia, em 2020.2, eu pensei em criar dois jogos, para as disciplinas de ADC (à época ARC) e Cabeamento Estruturado (CAB). O primeiro foi feito em Javascript, com Phaser, enquanto que o segundo foi com Twine. Embora com propostas bastante distintas, [ambos deveriam terminar juntos](https://youtu.be/AdRE60RLdYk). Infelizmente, assim como em todos os outros casos, os jogos não foram terminados - eles cumpriam seu papel mais rápido do que eu gostaria...

Vou aproveitar, assim, essas histórias inacabadas para este _chatbot_...

## Premissa do jogo

Dois irmãos foram separados do pai no começo da Grande Pandemia, e querem se reencontrar. O filho, mais velho, está tentando fugir da sua ARCa (assim chamados os prédios usados para as bolhas sociais), enquanto a filha, presa em outra ARCa, está tentando encontrá-los através dos sistemas ligados a Internet.

## O jogo ideial

O cenário é pós-apocalíptico. A pandemia do Covid-19, rapidamente, torna-se a Grande Pandemia. Incontáveis mutações ocorrem em todo o planeta. De uma forma ainda não totalmente entendida, o DNA parece ser a semente aleatória das mutações. Assim, as famílias são isoladas entre si. Grande prédios são construídos, as ARCas, para abrigar essas bolhas sociais, e máquinas assumem papéis essenciais na vida, agora transformada. A Grande Máquina emerge como a nova ordem mundial.

Porém, uma família, na tentativa de fugir do controle, é fragmentada. O pai, descoberto mexendo nos sistemas da Grande Máquina, [teve sua consciência assimilada por ela](https://boidacarapreta.github.io/arc20201/). O filho mais velho se sustenta com alguns bicos na sua ARCa, e [é convidado por um estranho a invadir os sistemas da Grande Máquina](https://boidacarapreta.github.io/integrado20212/cliente/). A filha, por fim, com a ajuda de uma amiga próxima, [vasculha os sistemas da Grande Máquina em busca de sinais dos parentes próximos](https://boidacarapreta.github.io/cab20202/).

O formato é uma homenagem aos clássicos como Zelda:

- [Mapa em 2D](https://boidacarapreta.github.io/adcipt20221/);
- Construções para entrar e interagir com personagens, como comprar ou mesmo trocar itens;
- Diálogos com as missões (principal e secundárias).

Ao entrar em uma partida, o jogo escolherá um dos dois personagens aptos a jogar: filho e filha. Cada um deve tomar decisões para chegar ao seu destino. O canal de áudio é imprescindível para este jogo: como cada jogador pode jogar com apenas um personagem, será necessário pelo menos 2 jogadores com papéis diferentes para desbloquear a cena final de reencontro dos filhos. Ou seja, vários jogadores podem assumir o papel de filho ou filha, mas somente um de cada conseguirá chegar na última cena, e a cooperação entre filho e filha será essencial nos momentos decisivos. Logo, o canal de áudio terá duas funções: som ambiente do jogo e permitir que os jogadores conversem entre si.

Em relação a programação, o _chatbot_ usará uma máquina de estado para cada jogador, que deverá conter:

- Personagem sorteado;
- Inventário (lista de objetos);
- Pergunta;
- Listas de respostas possíveis. Para cada resposta:
  - Objetos necessários;
  - Próximo estado.

Dessa forma, a programação do _chatbot_ será feita de forma independente do jogo em si. Enquanto que aquele cuida da interação do usuário (texto e voz), a máquina de estado, a ser armazenada em banco de dados a parte, define a mecânica do jogo.

Em essência, ambos, filho e filha, devem se encontrar para encontrar o pai, que está preso dentro da Grande Máquina.

## Referências

Eu sempre escolho uma música para ambientação quando começo a me concentrar no jogo. Enquanto que no semestre passado eu escutei [The Pretender, do Foo Fighters](https://open.spotify.com/track/7x8dCjCr0x6x2lXKujYD34?si=14cdb7ba4a304513), este semestre o ponto de partida vem de [You're Always in Time, do Tangerine Dream](https://open.spotify.com/track/5EexQPDX4zS2jVq7lloRc3?si=96ac0da218fb4b1c).

Para a situação do pai, nada mais óbvio que [Neuromancer](https://editoraaleph.com.br/produto/neuromancer/). Para os filhos, [Incal](https://pipocaenanquim.com.br/produto/incal-volume-1-da-serie-todo-incal/) é sem dúvida a maior influência, principalmente essa mistura entre ciência e religião.

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

### Em todas as IDEs baseadas em VSCode (incluindo Gitpod)

O arquivo `.vscode/launch.json` tem uma entrada para o arquivo `chatbot.py` para execução e depuração.
