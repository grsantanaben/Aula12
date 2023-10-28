##CONJUNTOS EM PYTHON
conjunto1 ={2,3,6,5}
conjunto2 ={10,7,9,40}

#Diferença entre os conjuntos
print(conjunto1.difference(conjunto2))
print(conjunto2.difference(conjunto1))

#Adicionar um dado
conjunto1.add(70)
print (conjunto1)
conjunto2.add(25)
print (conjunto2)

# #Remover dados do conjunto (remove ou discart) (Não permite remover o indice[])
conjunto1.remove(2)
print (conjunto1)


#**Verificando a existência de elementos:**
conjunto1 ={10,2,3,6,5}
conjunto2 ={10,7,9,40}
if 10 in conjunto1:
print ('Existe o elemento 10')
v =len(conjunto1)
print(v)  

#Exercicios 


#1: Crie um conjunto chamado "frutas" com as seguintes frutas: maçã, banana, laranja, pêra e abacaxi. Em seguida, imprima o número de elementos no conjunto.

frutas = {'maça', 'banana', 'laranja', 'pêra','abacaxi', 'Uva'}
print(len(frutas))

#2: Crie dois conjuntos, "conjunto1" e "conjunto2", #com alguns números inteiros. Imprima a união desses dois conjuntos

num1 = {1,2,3,4,5,}
num2 = {6,7,8,9,10}
print(num1.union(num2))

#3: Dado o conjunto "cores" com cores diferentes, remova a cor "vermelho" do conjunto.
cores = {'vermelho', 'azul', 'amarelo', 'verde', 'Rosa','Branco'}
print (cores)
cores.remove('vermelho')
print(cores)

#4: Crie um conjunto chamado "numeros" com os números de 1 a 10. 
#Em seguida, crie um novo conjunto chamado "pares" contendo apenas os números pares do conjunto "numeros".

numeros = {1,2,3,4,5,6,7,8,9,10}
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

#5: Verifique se o conjunto "alunos_aprovados" contém todos os alunos do conjunto "todos_alunos". Os conjuntos devem ser definidos com nomes apropriados

t_a = {'João', 'Maria', 'José', 'Pedro', 'Ana', 'Carla','Gabriel','Bea'}
a_a = {'João', 'Maria', 'José', 'Pedro', 'Ana','carla'}
print (t_a.intersection(a_a))
