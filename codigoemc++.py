/*
* Autor: Rafaela Cardoso
* Linguagem: C++
* Data: 14/12/2024
* Descrição: Programa que mostra o seu nome, cidade e idade digitada no console.
* Funcionalidades: As strings nome e cidade e varivel int idade foram criadas e, usando cout é perguntado ao usuario seu nome, que será armazenado na variavel "nome", após isso será perguntado sua cidade, que a resposta será armazenada na variavel "cidade" e, por ultimo é perguntado sua idade, que será armazenado na variavel "idade". Por final, será mostrado no console a seguinte mensagem - "Olá + variavel nome. Você mora em + variavel cidade e tem + variavel idade.
* Versão: [1.0]
*/


#include <iostream>
#include <string> // necessário para usar strings no C++

using namespace std;

int main() {
  // variavel que armazena o nome digitado
    string nome;
  // variavel que armazena a cidade digitada
    string cidade;
  // variavel que armazena a idade digitada
    int idade;

  // comando que faz com que apareça no console a mensagem "Qual seu nome?"
    cout << "Qual seu nome? " << endl;
    cin >> nome; // Comando que faz a leitura do nome digitado

  // comando que faz com que apareça no console a mensagem "Qual sua cidade?"
    cout << "Qual sua cidade? " << endl;
    cin >> cidade; // comando que faz a leitura da cidade

  // comando que faz com que apareça no console a mensagem "Qual sua idade?"
    cout << "Qual sua idade? " << endl;
    cin >> idade; // comando que faz a leitura da idade

    // exibe a mensagem abaixo 
    cout << "Olá, " << nome << ". Você mora em " << cidade << " e tem " << idade << " anos." << endl;

    return 0;
}
