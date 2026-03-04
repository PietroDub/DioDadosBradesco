//Calcule e imprima o salário
//receba o valor bruto e os benefícios

//imposto:
// 1100 > = 5%
// 2500 > = 10%
// 2500 < = 15%

// scanner (é o input), system.out.println (é o output)

import java.util.Scanner;

public class Desafio {

    public static void main(String[] args) {
    //Lê os valores de Entrada:
    Scanner leitorDeEntradas = new Scanner(System.in);
    float valorSalario = leitorDeEntradas.nextFloat();
    float valorBeneficios = leitorDeEntradas.nextFloat();

    float valorImposto = 0;
    if (valorSalario >= 0 && valorSalario <= 1100) {
    //Atribui a alíquota de 5% mediante o salário:
    valorImposto = 0.05F * valorSalario;
    } else if (valorSalario >= 1100.01 && valorSalario <= 2500.00) {
    valorImposto = 0.10F * valorSalario;
    }else (valorSalario > 2500) {
    valorImposto = 0.15F * valorSalario;
    }
    //TODO Criar as demais condições para as alíquotas de 10.00% e 15.00%.

    //Calcula e imprime a Saída (com 2 casas decimais):
    float saída = valorSalario - valorImposto + valorBeneficios;
    System.out.println(String.format("%.2f", saída));
    }
}