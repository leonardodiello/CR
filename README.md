# Calculadora de CR

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-success)](https://github.com/leonardodiello/CR)
[![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)](https://github.com/leonardodiello/CR)

## Sobre o projeto

Este projeto consiste em uma **Calculadora de Coeficiente de Rendimento (CR)** desenvolvida em Python.

A aplicação permite informar as disciplinas cursadas, suas respectivas notas e cargas horárias para calcular o Coeficiente de Rendimento do período.

O projeto foi desenvolvido como parte dos estudos de **Introdução à Python para Ciência de Dados**, aplicando conceitos fundamentais de programação e lógica.

## Funcionalidades

* Definição da quantidade de disciplinas.
* Entrada das notas de cada disciplina.
* Entrada da carga horária de cada disciplina.
* Cálculo do CR utilizando média ponderada pela carga horária.
* Possibilidade de informar o CR de períodos anteriores.
* Cálculo do CR atualizado.
* Exibição do resultado com duas casas decimais.

## Cálculo

O CR é calculado considerando a carga horária de cada disciplina como peso:

```text
CR = Σ(nota × carga horária) / Σ(carga horária)
```

Dessa forma, disciplinas com maior carga horária possuem maior peso no cálculo.

## Tecnologias utilizadas

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)

* Python.
* Git.
* GitHub.
* Visual Studio Code.

## Como executar

### Clone o repositório

```bash
git clone https://github.com/leonardodiello/CR.git
```

### Entre na pasta

```bash
cd CR
```

### Execute o programa

```bash
python FIC.py
```

Caso esteja utilizando um sistema em que o comando `python` não esteja disponível:

```bash
python3 FIC.py
```

## Exemplo

```text
Esse é um programa que ajuda você a calcular o seu Coeficiente de Rendimento.

Quantas matérias você tem? 3

Digite a média da 1ª matéria: 8.5
Digite a carga horária da 1ª matéria: 60

Digite a média da 2ª matéria: 9.0
Digite a carga horária da 2ª matéria: 80

Digite a média da 3ª matéria: 7.5
Digite a carga horária da 3ª matéria: 60

CR atual: 8.35
```

## Estrutura do projeto

```text
CR/
├── FIC.py
└── README.md
```

## Conceitos praticados

Durante o desenvolvimento foram aplicados conceitos fundamentais de Python, incluindo:

* Variáveis.
* Tipos de dados.
* Entrada e saída de dados.
* Conversão de tipos.
* Estruturas condicionais.
* Estruturas de repetição.
* Operações matemáticas.
* Média ponderada.
* Lógica de programação.

## Objetivo

O principal objetivo do projeto foi colocar em prática conceitos de programação em Python por meio do desenvolvimento de uma aplicação simples e útil para estudantes.

Além de servir como uma calculadora de CR, o projeto representa uma etapa dos meus estudos em **Python e desenvolvimento de software**.

## Autor

**Leonardo Diello Charão**

Estudante de Engenharia de Software.

[![GitHub](https://img.shields.io/badge/GitHub-leonardodiello-181717?style=for-the-badge\&logo=github)](https://github.com/leonardodiello)
