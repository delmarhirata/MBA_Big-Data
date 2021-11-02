#!/usr/bin/env python
# coding: utf-8

# **Desafio #01.**
# 
# Pegue o seguinte texto:
# 
# Um forte indicador de que já há avanços de Democratização de Dados nas organizações é observar quantas pessoas tem acesso a Dados.
# 
# - Conte a quantidade de letras no texto e também a quantidade de letras repetidas.

# In[35]:


# Conta a quantidade de carcteres.
def contador_carcter(texto):
    contador = 0
    for caracter in texto:
        contador += 1
    return contador

# Manta uma lista com carcteres exclusivos
def monta_lista_exclusivo(texto):
    n_frase = []
    cont1 = 0
    cont2 = 0
    while contador_carcter(texto) > cont1:    
        try:
            n_frase.index(texto[cont1])
            cont1 += 1
        except:
            n_frase.append(texto[cont1])
            cont1 += 1
            cont2 += 1
    return n_frase

# Impressão das ocorrencias
def ocorrencias(texto):
    con = 0
    cont = 0
    while contador_carcter(monta_lista_exclusivo(texto)) > con: 
        for i in range (contador_carcter(texto)):
            if texto[i] == monta_lista_exclusivo(texto)[con]:
                cont += 1 
        print( 'O Caracter: "{}" repete {} vez(es).'.format(monta_lista_exclusivo(texto)[con], cont))
        con += 1
        cont = 0


# In[36]:


# Entra com a frase a ser analisada
texto = str(input("Digite a Frase: "))


# In[37]:


# Impressão do resultado
print('Esta frase tem {} caracteres. Incluindo espaços e pontuação.'.format(contador_carcter(texto)))
print('Esta frase tem {} caracteres distintos. Incluindo espaços e pontuação.'.format(contador_carcter(monta_lista_exclusivo(texto))))
print()
print('Aqui estão as ocorrencias:')
ocorrencias(texto)


# In[ ]:




