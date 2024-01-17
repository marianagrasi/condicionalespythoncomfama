#Toda lista se debe escribir en plural
arboles=['ceiba', 'yarumo', 'manzano', 'guayacan']
municipios=['Medellin', 'Titiribi', 'Carolina del principe']
hectareasSembradas=[2500,500,1200]
lluviasMayoresA500=[False,True, True]
#Recorriendo  un arreglo
#Acceder de forma dinamica el contenido de un arreglo
#Para recorrerlo debo utilizar un ciclo o bucle o loop 

#Ciclo while (mientras)= que hago mientras se cumple la condicion
#contador=revisa la ejecucion del ciclo y pone los frenos 
'''contador=0
while contador<10:
    contador=contador+1
    print("Estoy triufando....")
'''
    #ciclo For (Para)
#for(contador=0; condicion;i=i+1)
#primer#= es desde donde empieza
#segundo#=hasta donde llega
#tercer#= de cuanto en cuanto va a contar.


'''for variableIretadora in range(1, 301,2):
    print(variableIretadora)'''

#Recorrer dinamicamente un arreglo usando un FOREACH (PARA CADA UNO)=
# TODO FOREACH TIENE UNA VARIABLE AUXILIAR

for arbol in arboles:
    print (arbol)

for municipio in municipios:
    print(municipio)

    









#Los datos de la lista deben ser del mismo tipo
#Si quiero almacenar datos de tipos diferentes no me sirve la lista o arreglo.
#Diccinario=Estructura de datos que permite almacenar muchos datos de tipos diferentes 
#se accede por poscicio eje arbole[2]
