#Linear Algebra: PageRank
Fundação Getúlio Vargas - Escola de Matemática Aplicada \
Bacharelado em Ciência de Dados \
Curso de Álgebra Linear \
Professor: Yuri Fahham Saporito \
Alunos: Gianlucca Devigili e Maisa O. Fraiz

## 1. Introdução
O presente trabalho aborda o algoritmo _PageRank,_ desenvolvido por Sergey Bin e Larry Page em 1996 para a organização do sistema de buscas do _Google,_ o qual são fundadores. O trabalho tem como objetivo explicar o que é o _PageRank,_ como calcular essa métrica usando álgebra linear e como ela pode ser aplicada nas mais diversas áreas de pesquisa. <br>
Por meio da implementação de uma adaptação do algoritmo, também busca calcular uma possível relevância das fronteiras dos estados dos EUA em um grafo não direcional das mesmas. Para tal, é feito o uso da linguagem de programação _Python_ e suas bibliotecas, tais como _networkx_ para gerar o grafo e _matplotlib_ para a visualização do mesmo.

## 2. O algoritmo _PageRank_
O _PageRank_ é um algoritmo criado por Sergey Brin e Larry Page, fundadores da multinacional _Google,_ em 1996. Ele foi criado com a função de servir como uma métrica para estimar a importância das páginas na internet, organizando o sistema de busca de forma que os resultados mais relevantes apareçam primeiro para o usuário. De acordo com Google (2020), o a relevância de uma página é calculada, dentre diversos outros fatores decorridos da sofisticação do algoritmo, através da relevância das páginas que possuem links que apontem para ela.<br>

