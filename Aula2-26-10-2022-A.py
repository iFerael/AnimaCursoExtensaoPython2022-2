#Comando input(): quero permitir que
#O usuário digite algo
nome = str(input("Digite seu nome: ")) 
idade = int(input("Qual sua idade? "))
#Comando de saída, exibir na tela
print(f"Boa noite, seu nome é {nome}")
print(f"Sua idade é {idade} anos")
#print(f"Sua idade é {}" .format (idade))

#Se eu quiser mostrar o dobro da idade?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

#estrutura condicional - o famigerado "SE" (if)
#Se a pessoa for maior de idade, motre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Vocé é maior de idade, ótimo! Já pode beber ou dirigir")
else:
 print("Você é jovem ainda, jovem!")

#E se eu quiser perguntar o gênero? (M = masculino e F = Feminino)
#Mostra (... e você também precisa ou precisou prestar o serviço militar obrigatório)


genero = str(input("Informe seu Gênero M = Masculino, F = Feminino, O = Outros "))
if idade >= 18 and genero == "M":
 print ("Você também precisa ou precisou prestar o serviço militar obrigatório")


print("vai ser executada de qualquer jeito")

