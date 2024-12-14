/*
* Autor: Rafaela Cardoso
* Linguagem: Java
* Data: 14/12/2024
* Descrição: Programa que conforme o número do mês que você nasceu for digitado, aparecerá o nome do mês correspondente.
* Funcionalidades: Solicita ao usuário o número do mês de nascimento.
Exibe o nome do mês correspondente ao número informado.
*/



import java.io.IOException;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    // comando que faz aparecer a mensagem "Qual o número do mês que você nasceu?" no console
    System.out.printf("Qual o número do mês que você nasceu?%n%n");

    // criei a variavel "val" e scaneei ela servindo como resposta para a pergunta acima, onde o valor será armazenado dentro desta variavel
    int val = input.nextInt();

  // se a variavel "val" (valor digitado) for igual a 1, no console aparecerá a mensagem "Você nasceu em janeiro."
    if (val == 1){
      System.out.printf("Você nasceu em janeiro.%n");
      // se a variavel "val" (valor digitado) for igual a 2, no console aparecerá a mensagem "Você nasceu em fevereiro."
    } if (val == 2){
      System.out.printf("Você nasceu em fevereiro.%n");
      // se a variavel "val" (valor digitado) for igual a 3, no console aparecerá a mensagem "Você nasceu em março."
    } if (val == 3){
      System.out.printf("Você nasceu em março.%n");
      // se a variavel "val" (valor digitado) for igual a 4, no console aparecerá a mensagem "Você nasceu em abril."
    } if (val == 4){
      System.out.printf("Você nasceu em abril.%n");
      // se a variavel "val" (valor digitado) for igual a 5, no console aparecerá a mensagem "Você nasceu em abril."
    } if (val == 5){
      System.out.printf("Você nasceu em maio.%n");
      // se a variavel "val" (valor digitado) for igual a 6, no console aparecerá a mensagem "Você nasceu em junho."
    } if (val == 6){
      System.out.printf("Você nasceu em junho.%n");
      // se a variavel "val" (valor digitado) for igual a 7, no console aparecerá a mensagem "Você nasceu em julho."
    } if (val == 7){
      System.out.printf("Você nasceu em julho.%n");
      // se a variavel "val" (valor digitado) for igual a 8, no console aparecerá a mensagem "Você nasceu em agosto."
    } if(val == 8){
      System.out.printf("Você nasceu em agosto.%n");
      // se a variavel "val" (valor digitado) for igual a 9, no console aparecerá a mensagem "Você nasceu em setembro."
    } if (val == 9){
      System.out.printf("Você nasceu em setembro.%n");
      // se a variavel "val" (valor digitado) for igual a 10, no console aparecerá a mensagem "Você nasceu em outubro."
    } if (val == 10){
      System.out.printf("Você nasceu em outubro.%n");
      // se a variavel "val" (valor digitado) for igual a 11, no console aparecerá a mensagem "Você nasceu em novembro."
    } if (val == 11){
      System.out.printf("Você nasceu em novembro.%n");
      // se a variavel "val" (valor digitado) for igual a 12, no console aparecerá a mensagem "Você nasceu em dezembro."
    } if (val == 12){
      System.out.printf("Você nasceu em dezembro.%n");
    }
    input.close();
  }

}
