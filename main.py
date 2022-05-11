'''Escreva um programa em linguagem Python para encontrar números entre 100 e 400 (ambos inclusos), onde cada dígito de um número é um número par, utilizando estruturas de repetição (3,0)'''
for num in range (100,401,2):
  par = str (num) #converter o numeros em strings
  if (int(par[0])%2==0) and (int(par[1])%2==0) and (int(par[2])%2==0): #verificando indice por indice na conversão
    print(par)
  