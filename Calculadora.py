#!/usr/bin/env python
# coding: utf-8

# In[12]:


class calculadora:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def soma(self):
        soma = self.num1 + self.num2
        print("O resultado da soma é: ", soma)

    def subtracao(self):
        subtracao = self.num1 - self.num2
        print("O resultado da subtração é: ", subtracao)

    def mutilicacao(self):
        mutilicacao = self.num1 * self.num2
        print("O resultado da mutiplicação é: ", mutilicacao)

    def divisao(self):
        if self.num2 == 0:
            divisao = "O resultado da divisão é: ERRO - O divisor tem que ser diferente que zero"
            print(divisao)
         
        else:
            divisao = self.num1 / self.num2
            print("O resultado da divisão é: ", divisao)


# In[13]:


num1 = input("Entre com o primeiro número: ")
num2 = input("Entre com o segundo número: ")


# In[14]:


calculadora = calculadora(num1, num2)
calculadora.soma()
calculadora.subtracao()
calculadora.mutilicacao()
calculadora.divisao()

