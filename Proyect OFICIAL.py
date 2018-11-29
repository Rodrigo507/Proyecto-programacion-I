totalinf = 0        #Total de infrapeso/Contador
totalnorm = 0       #Total de normal/Contador
totalsobr = 0       #Total de sobrepeso/Contador
totalobs = 0        #Total de obesidad/Contador
totalhom = 0        #Total de masculinos/Contador
totalmuj = 0        #Total de Mujeres/Contador
mayortalla = 0      #Almacena la mayor talla del censo
nomayortalla = ''   #Almacena el nombre de la mayor talla del censo
acumedad = 0        #Suma la edad de todo los niños del censo
niños = 0           #Contador de niños del censo
adolecente = 0      #Contador de adolecentes
adulto = 0          #Contador de adulto
terceraedad = 0     #Contador de tercera edad
obsm = 0            #El total de personas con obesidad masculino
obsf= 0             #El total de personas con obesidad mujeres
menorpeso=800       #Almacena el menor peso del censo
nombmenorpesos= ''  #Almacena nombre del menor peso del censo
po=0                #Centinela para niña con infrapeso
ad=0                #Centinela de El adulto de menor peso
conta=0             #Contador para saber el numero de paciente automaticamente
nmayortalla= 0      #Almacena el numero de la persona de mayor talla
ncensadomenorpeso=0 #Almacena el numero de la persona de menor peso solo de Adultos
edadprom = 0        #Almacena la edad promedio de los niños
resp = 'si'         #Controlador del ciclo
print ("Instrucciones".center(70, "=" ),'\n', "Llene el formulario de la siguiente manera".center(70," "))
print('\n', "En nombre debe de introducir el nombre de la persona a censar".center(70," "),'\n', "Sexo Utilice “F” si es femenino y “M” si es masculino".center(70," "))
print ("En edad debe de introducir la edad de forma numérica “12”".center(70, " " ),'\n', "En peso  se tendrá que dar el mismo  en libras".center(70," "))
print("Talla o la estatura se tendrá que introducir en metros".center(70," "))
print("Para tomarle los datos a otra persona responda “SI”o“si”".center(70," "))
print("Para salir digite un “NO” o “Otro carácter”".center(70," "))
print("____________________________________________________________________________")
while resp == 'si' or resp== 'SI':
    conta=conta+1
    nomb = input("Nombre: ")  #La variable almacena el dato preguntado "El nombre"
    sexo = input("Sexo: ")  #almacena el dato preguntado "Sexo de la persona censada"
    edad = int(input("Edad: "))  #almacena la edad "Edad"
    peso = int(input("Peso Libras: "))  #Captura el peso  en libras
    talla = float(input("Talla o estatura mts: "))  #Captura la talla o altura en metros
    pesomlg = peso / 2.2046  #Se  transforma el peso de libras en KLG
    imc = pesomlg / (talla * talla)  #La variable imc almacena el índice de masa corporal
        
    if talla >= mayortalla: #Se hace la comparacion para saber la mayor talla del censo
        mayortalla = talla  #Almacena la talla de la persona de mayor talla
        nomayortalla = nomb #Almacena el nombre de la persona de mayor talla
        nmayortalla=conta   ##Almacena el numero de censado  de la persona de mayor talla
    if imc < 18.50: #Se compara para saber en si el censado esta en Infrapeso
        print("El IMC de ", nomb, "es: ", '%.2f' % imc, " Infrapeso")
        totalinf = totalinf + 1 #Contador de persona con infrapeso
    
    else:
        if imc >= 18.50 and imc <= 24.99: #Se compara para saber en si el censado esta en Normal
            print("El IMC de ", nomb, "es: ", '%.2f' % imc, " Normal")
            totalnorm = totalnorm + 1 #Contador de persona con Normal
        
        else:
            if imc >= 25.00 and imc <= 29.99: #Se compara para saber en si el censado esta en Sobrepeso
                print("El IMC de ", nomb, "es: ", '%.2f' % imc, " Sobrepeso")
                totalsobr = totalsobr + 1 #Contador de persona con sobrepeso
            
            else:                                                            
                if imc >= 30.00: #Se compara para saber en si el censado esta en Obesidad
                    print("El IMC de ", nomb, "es: ", '%.2f' % imc, " Obesidad")
                    totalobs = totalobs + 1 #Contador de persona con Obesidad                                  
                    
    if sexo == 'm' or sexo == 'M': #Se busca saber de que sexo es el censado y se cuenta
        totalhom = totalhom + 1 #Contador sexo masculino
    else:
        if sexo == 'f' or sexo == 'F':
            totalmuj = totalmuj + 1 #Contador sexo femenino
    if edad >= 0 and edad <= 12: #Si la edad esta entre 0 y 12 es niño 
        niños = niños + 1 #Contador de niños
        acumedad = acumedad + edad #Acumulador de edad
    else:
        if edad > 12 and edad <= 18: #Si la edad esta entre 13 y 18 es adolecente y se cuenta
            adolecente = adolecente + 1  #Contador de adolecentes
        else:
            if edad > 18 and edad <= 60: #Si la edad esta entre 19 y 60 es adulto y se cuenta
                adulto = adulto + 1 #Contador de adultos
                if menorpeso >= peso: #Se busca el menor peso solo de Adultos y se actualiza el nombre y peso 
                        menorpeso=peso
                        nombmenorpesos = nomb
                        ncensadomenorpeso=conta
                        ad =1 #se actualiza la centinela a 1 
            else:#Si la edad es mayor a 60 es detercera edad y se cuenta}
                terceraedad = terceraedad + 1 #Contador de tercera edad
                    
    if sexo == 'f' and imc >= 30.00: #personas con obesidad por sexo.
        obsf = obsf + 1 #Contador de obesidad mujeres
    if  sexo == 'm' and imc >= 30.00: #personas con obesidad por sexo.
        obsm = obsm + 1 #Contador de obesidad hombres
    if edad <=12 and sexo == "f" and imc <=18.50:  #niña con infrapeso y se actualiza la centine l
        po=1 
    resp = input("Desea continuar: ") #pregunta que controla al ciclo
    print("____________________________________________")
                      #SE TERMINA EL CICLO
#FUERA DEL CICLO
if ad==0: # Si no hay adulotos en el censo se imprimira el siguiente mensaje
    menorpeso='**'
    nombmenorpesos='No hay Adulto en el censo'

if niños != 0: #Solo entrara si hay niños y si no se imprimira "No hay niños en el censo"
	edadprom = acumedad / niños #Saca el promedio de las edades de niños
else:
		edadprom = "No hay niños en el censo"
if po == 1: #si la centinela se actualiza 1 entrara e imprimira el siguiente mensaje
    niñainfr="Hay almenos 1 Niña con infrapeso"
else:
    niñainfr = ''
print("RESULTADO DEL CENSO".center(65,"*"))
print("El total de personas infrapeso,normal,sobrepeso,obesidad".center(65,"*"))
print("Total persona Infrapeso ", totalinf) #Se imprimira el Total de personas con infrapeso
print("Total persona Normal ", totalnorm) #Se imprimira el Total de personas con peso normal
print("Total persona Sobrepeso ", totalsobr) #Se imprimira el Total de personas con sobrepeso
print("Total persona Obesidad ", totalobs) #Se imprimira el Total de personas con obesidad
print("El total de masculino y femenino".center(65,"*"))
print("Total de hombres censados", totalhom) #Se imprimira el Total de hombres censado
print("Total de mujeres censados", totalmuj) #Se imprimira el Total de mujeres censado
print("La persona de mayor talla".center(65,"*"))
print("Nombre de la persona de mayor talla")
print("Censado #", nmayortalla, nomayortalla, "y la talla es ", mayortalla) #Se imprimira el nombre de la pesona con mayor talla y su talla.
print("Total niños, adolescentes, adultos y tercera edad".center(65,"*"))
print("Total de ninos ", niños) #Se imprimira el Total de niños censado
print("Total de adolecente ", adolecente) #Se imprimira el Total de adolecentes censado
print("Total de adulto", adulto) #Se imprimira el Total de adultos censado
print("Total de tercera edad", terceraedad) #Se imprimira el Total de tercera edad censado
print("La edad promedio de los niños".center(65,"*"))
print(edadprom) #Se imprimira la edad promedio de niños censado
print("Total de personas con obesidad por sexo".center(65,"*"))
print("Homres: ", obsm, "Mujeres: ", obsf) #Se imprimira el Total de hombres y mujeres por ceparado con obesidad
print("El adulto de menor peso".center(65,"*"))
print("Censado #", ncensadomenorpeso ,nombmenorpesos, "peso: ", menorpeso) #Se imprimira el nombre de del adulto con menor peso y su peso
print(niñainfr) #Si hay una niña con infrapeso en el censo se imprimira el mensaje de niña con infrapeso
