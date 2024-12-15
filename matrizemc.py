/*
* Autor: Rafaela Cardoso
* Linguagem: C
* Data: 14/12/2024
* Descrição: Programa que exibi a posição dos vetores digitados e as posições dentro de uma matriz.
* Funcionalidades: 
- O programa pede ao usuário que insira 5 números e armazena os números em um vetor de tamanho 5.
- Para a exibição do vetor:
Pede que o usuário insira 9 números e armazena os números em uma matriz 3x3, depois mostra os números armazenados no vetor.
- Mostra os números armazenados na matriz (3 linhas e 3 colunas).
Para cada linha da matriz, calcula a soma dos elementos.
Exibe a soma de cada linha.
* Versão: [1.0]
*/


#include <stdio.h>

int main() {
    // Criei um vetor de tamanho 5
    int vetor[5];
  //comando que faz com que apareça a mensagem "Digite 5 números para preencher o vetor:" no console
    printf("Digite 5 números para preencher o vetor:\n");
  // criei a variavel i que vale 0, enquanto i for menor que 5, i será somado em 1 em 1
    for (int i = 0; i < 5; i++) {
      //comando que faz aparecer no console a mensagem "Número %d:(valor de i) ", fazendo i + 1
        printf("Número %d: ", i + 1);
      // scaneei o vetor para que a variavel i entrasse dentro dele
        scanf("%d", &vetor[i]);
    }

    // comando que exibe o vetor
    printf("Vetor preenchido:\n");
  // criei a variavel i, enquanto menor de 5, i será somado em 1 em 1
    for (int i = 0; i < 5; i++) {
      // mostra os numeros digitados que preenchem o vetor
        printf("%d ", vetor[i]);
    }
    printf("\n");

    // criei uma matriz 3x3
    int matriz[3][3];
  //comando que faz aparecer a mensagem "Digite 9 números para preencher a matriz 3x3:"
    printf("\nDigite 9 números para preencher a matriz 3x3:\n");
  // criei a variavel i que quando for menor que 3 será somada em 1 em 1, equivale as 3 linhas da matriz
    for (int i = 0; i < 3; i++) {
      // criei a variavel j que quando for menor que 3 será somada em 1 em 1, equivale as 3 colunas da matriz
        for (int j = 0; j < 3; j++) {
          // numero da posição da linha e coluna que o numero vai estar
            printf("Número para a posição [%d][%d]: ", i, j);
          //scaneei a matriz para que dentro dela estivesse a posição i e j
            scanf("%d", &matriz[i][j]);
        }
    }

    // comando que faz aparecer no console a mensagem "Matriz preenchida:"
    printf("\nMatriz preenchida:\n");
  // criei a variavel i que quando for menor que 3 será somada em 1 em 1
    for (int i = 0; i < 3; i++) {
      // criei a variavel j que quando for menor que 3 será somada em 1 em 1
        for (int j = 0; j < 3; j++) {
          // mostra a matriz com as posições i e j 
            printf("%d ", matriz[i][j]);
        }
      //comando que pula linha
        printf("\n");
    }

    // Exemplo de soma de cada linha da matriz
    printf("\nSoma de cada linha da matriz:\n");
  // criei a variavel i que quando for menor que 3 será somada em 1 em 1
    for (int i = 0; i < 3; i++) {
      // criei a variavel somaLinha 
        int somaLinha = 0;
      // criei a variavel j que quando for menor que 3 será somada em 1 em 1
        for (int j = 0; j < 3; j++) {
          // somaLinha é igual i somado a j
            somaLinha += matriz[i][j];
        }
      //comando que exibe no console "Soma da linha %d: %d"
        printf("Soma da linha %d: %d\n", i + 1, somaLinha);
    }

    return 0;
}
