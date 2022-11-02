# Convencendo com números seu amigo programador
![Array sendo criada](https://github.com/cosmicpb/PresidentGraph/blob/main/img/flag.png?raw=true)

Você sabe o que é a **Navalha de Occam**?
É um princípio científico que postula que entre um conjunto de hipóteses, a que for mais simples ou tiver o menor número de premissas é, normalmente, a verdadeira.

No dia 30/10/2022 um novo Presidente do Brasil foi eleito democraticamente. No mesmo instante, diversos apoiadores de seu principal adversário começaram a criar teorias de conspiração, principalmente depois de gráficos relacionados à apuração começarem a ser divulgados na interwebs.

Boa parte desses teóricos de conspiração diziam que o gráfico não apresentava uma "curva natural", ou seja, uma curva que não se adequasse a qualquer realidade de apuração mundial.

Este artigo tem como objetivo apresentar argumentos contra a conspiração de fraude nas urnas eleitorais em 2022, demonstrando a facilidade em se gerar um gráfico próximo ao obtido com a média agregada da apuração utilizando apenas duas premissas simples:

1. Os votos são contados inicialmente em locais com maioria de um candidato (Candidato 1);
2. Os votos são contados paralelamente, ou seja, diversas urnas são apuradas e contabilizadas ao mesmo tempo.


Portanto:
1. Os votos são contados digitalmente, ou seja, a vazão de votos (número de votos contados por minuto) cresce no início mas em suma é constante.
2. No gráfico temos o Candidato 1 (em azul) e o Candidato 2 (em vermelho). As primeiras zonas a serem contabilizadas foram as do Sul e as últimas do Nordeste, portanto com alta taxa para o Cand1 no início e alta taxa para o Cand2 no final.
3. Para cada candidato foram criadas duas arrays com médias representando o valor final de votação:
    * Primeira Array: Aleatória Ordenada (Decrescente para o Cand1 e Crescente para o Cand2);
    ![Array sendo criada](https://github.com/cosmicpb/PresidentGraph/blob/main/img/code.png?raw=true)

    
    * Segunda Array: Aleatória


4. Foi criada também uma terceira array, em que os valores das outras duas já criadas se intercalavam, de tal forma que:
    * Array3[0] = Array1[0]
    * Array3[1] = Array2[0]
    * Array3[2] = Array1[1]
    * Array3[3] = Array2[1]


Para o gráfico, foi utilizada a MÉDIA AGREGADA, ou seja, a média dos votos já computados.

Há um terceiro gráfico gerado com a força de voto para cada contagem, ou seja, a primeira vale 100% dos votos, a segunda 50%, a terceira 33%, e assim por diante, seguindo a função:

$$ forcVoto = {100 \over número de secoes apuradas} $$

Gráfico final:

![Gráfico final](https://github.com/cosmicpb/PresidentGraph/blob/main/img/finalgraph.png?raw=true)

## IMPORTANTE
Este código demonstra a facilidade em se criar, com apenas duas premissas, as condições necessárias para se criar este tipo de gráfico.

Este código não demonstra a facilidade em se fraudar as urnas, mas ao contrário: qualquer hipótese que leve em consideração fraude nas urnas gera premissas extremamente complexas como "manipulação no TSE", "conspiração entre juristas e fiscais", além das próprias Forças Armadas que também participaram do processo Eleitoral. **Neste caso, esse conjunto de premissas complexas quebra a Navalha de Occam.**


## Instação

Faça o download do código utilizando GIT ou utilize o ZIP disponível aqui no portal do GitHub.

```sh
git clone https://github.com/cosmicpb/PresidentGraph.git

```

Instale as dependências

```sh
cd PresidentGraph
pip install -r requirements.txt
```

## Usando o script:
```sh
python3 .\create_graph.py
```


Developed by Paulo Baldacim Junior
https://www.linkedin.com/in/paulobaldacimjunior/
https://twitter.com/memory_heap

**FREE ASSANGE**

**Free Software, Hell Yeah!**
