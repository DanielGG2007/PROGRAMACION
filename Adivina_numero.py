import random

numero_secreto = random.randint(1, 100)
adivinando = False

print ("adivina el numero")
   
while adivinando == False:
     
      intento = int(input("introduce el numero: "))
 
      if intento < numero_secreto:
         
          print("demasiado bajo")

      elif intento > numero_secreto:
         
          print("demasiado alto")

      else:
           print(f"correcto, el numero secreto era {numero_secreto}. ")
           adivinando = True