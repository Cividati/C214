# Questão 1
Api desenvolvida em flask para ordenação de arrays nuéricos através de algorítmos como bubble sort, insertion sort, heap sort, merge sort e bogo sort.

## Como começar

### 1. Instalando as Dependências
```bash
pip install -r requirements.txt
```
| **Lib** | **Versão** |
|----------|------------|
| pysort   | 1.0.0      |
| flask    | 2.1.2      |
| pytest   | 7.1.2      |


### 2. Rodando o web server
```bash 
python main.py
```

### 3. Alternar entre os algoritmos
Para acessar os diversos algoritmos, escolha o caminho desejado
| **Caminho**      |
|----------------|
| /bubblesort    |
| /insertionsort |
| /heapsort      |
| /mergesort     |
| /bogosort      |

Exemplo
localhost:80/bogosort

### 3. Passando o array de numeros
Para inputar o seu array desordenado, passe o argumento array na sua url.
| **Argumentos** | **tipo**         | **Exemplo**    |
|----------------|------------------|----------------|
| array          | lista de números | ?array=5,3,2,1 |

#### Exemplo

localhost:80/bogosort?array=5,4,3,2,1

## Autor
- [Rubens Cividati](github.com/Cividati)