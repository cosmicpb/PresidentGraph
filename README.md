# PresidentGraph

No dia 30/10/2022 um novo Presidente do Brasil foi eleito democraticamente.
No mesmo instante, diversos apoiadores de seu principal adversário começaram a criar teorias de conspiração, principalmente depois de gráficos relacionados à apuração começaram a ser divulgados na interwebs.

Boa parte desses teóricos de conspiração diziam que o gráfico não apresentava uma "curva natural", ou seja, uma curva que não se adequasse a qualquer realidade de apuração mundial.

Existem algumas premissas para esse projeto:
1. Os votos são contados digitalmente, ou seja, a vazão de votos (número de votos contados por minuto) é constante;
2. No gráfico temos o Candidato 1 (em azul) e o Candidato 2 (em vermelho). As primeiras zonas a serem contabilizadas foram as do Sul e as últimas do Nordeste, portanto com alta taxa para o Cand1 no início e alta taxa para o Cand2 no final.
3. Para cada candidato foram criadas duas arrays com médias representando o valor final de votação:
    * Primeira Array: Aleatória Ordenada (Decrescente para o Cand1 e Crescente para o Cand2);
    * Segunda Array: Aleatória
4. Para cada candidato foi criada também uma terceira array, em que os valores das outras duas já criadas se intercalavam, de tal forma que:
    * Array3[0] = Array1[0]
    * Array3[1] = Array2[0]
    * Array3[2] = Array1[1]
    * Array3[3] = Array2[1]


Para o gráfico, foi utilizada a MÉDIA AGREGADA, ou seja, a média dos votos já computados.


## Instação

Faça o download do código utilizando GIT ou utilize o ZIP disponível aqui no portal do GitHub.

```sh
git clone https://github.com/cosmicpb/2022-brelections-Apuration.git

```

Instale as dependências

```sh
cd 2022-brelections-Apuration
pip install -r requirements.txt
```

## Usando o script:
```sh
python3 .\apur.py
```


Developed by Paulo Baldacim Junior
https://www.linkedin.com/in/paulobaldacimjunior/
https://twitter.com/memory_heap

**Free Software, Hell Yeah!**


;