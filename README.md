# media-catalog
[work in progress]

## Objetivo
Quando eu comecei a estuar Python, pensei em codar um script simples pra resolver algum problema pessoal. Aí surgiu a ideia do media-catalog.

Eu tinha uma quantidade razoável de filmes em um HD externo (e que precisa de tomada, então não é muito portátil). Pra facilitar a visualização dos filmes que eu tinha no diretório, pensei em criar algum script que catalogasse os filmes em uma planilha, separados por título e ano. Dessa forma eu não preciso acessar sempre o HD pra saber quais filmes tenho.

Por enquanto é um script bem simples e espero melhorá-lo, adicionar mais informações e até mesmo trabalhar com APIs de databases, como IMDb e Letterboxd.

Outro objetivo é criar outro script que catalogue diretórios de álbuns de música também.

Toda colaboração é bem-vinda!
  

## Como usar

Somente o Python instalado é necessário.

O script espera que os diretórios dos filmes estejam nomeados como: "Título [Ano]"

Sendo que o ano pode estar dentro de parênteses também, ou qualquer outra coisa, afinal o script manipula a string de acordo com a posição dos caracteres.

Ou seja, ambos os seguintes exemplos seriam catalogados corretamente pelo script:

> The Big Lebowski [1998]

> Ghost In The Shell (1995)
  

Após isso, basta inserir o endereço do diretório a ser catalogado na variável **dir_filmes**, e o output desejado da planilha csv na variável **dir_csv**.

Após configurado o diretório, basta rodar o arquivo .py no terminal.