#!/usr/bin/env python
# coding: utf-8

# **Exercício #01**
# 
# A partir dos conhecimentos em sala de aula crie uma **calculadora**. Ela deverá receber dois valores. Após isso executar os metodos:
# - soma
# - subtracao
# - multiplicacao
# - divisao
# 
# Lembre-se na divisão testar o zero.

# In[9]:


# Criação da classe calculadora
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
        if self.num2 == 0: # teste do zero
            divisao = "O resultado da divisão é: ERRO - O divisor tem que ser diferente que zero"
            print(divisao)
        else:
            divisao = self.num1 / self.num2
            print("O resultado da divisão é: ", divisao)


# In[10]:


#Entrada dos números
num1 = input("Entre com o primeiro número: ")
num2 = input("Entre com o segundo número: ")


# In[11]:


# Executando calculadora
calculadora = calculadora(num1, num2)
calculadora.soma()
calculadora.subtracao()
calculadora.mutilicacao()
calculadora.divisao()


# In[ ]:




