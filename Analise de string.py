#!/usr/bin/env python
# coding: utf-8

# In[46]:


frase = str(input("Digite a Frase: "))
contador = 0
for caracter in frase:
    contador += 1

n_frase = []
cont1 = 0
cont2 = 0
while contador > cont1:    
    if len(n_frase) == 0:
        n_frase.append(frase[cont1])
        cont1 += 1
        cont2 += 1
    else:
        try:
            n_frase.index(frase[cont1])
            cont1 += 1
        except:
            n_frase.append(frase[cont1])
            cont1 += 1
            cont2 += 1
            
cont0 = 0
for caracter in n_frase:
    cont0 += 1

print("O total de caracteres é {}.".format(contador))
print("O total de caracteres distintos é {}.".format(cont0))
print("o número de caracteres repetidos é {}.".format(contador-cont0))

