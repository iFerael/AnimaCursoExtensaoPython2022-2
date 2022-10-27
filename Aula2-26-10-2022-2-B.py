#Pede o nome do aluno e sua noota ( de 0 a 10) e, se ele tirou nota 10, mostra "Você é bichão mesmo"
nome = str(input("Qual seu nome? "))
nota = float(input("Digite sua nota: "))
if nota == 10:
 print(f"{nome}, você é bichão mesmo")
elif (nota >=6.0 and nota <10.0):
  print("Parabéns, precisa estudar mais")
elif (nota >10.0):
  print(f"Essa nota não existe!")
else:
  print("Burro, não tirou dez")
