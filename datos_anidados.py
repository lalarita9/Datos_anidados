"""
Recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas: 
1 [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Si el primer número de la sublista es cero, omitir la impresión de toda la sublista.
• Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
"""
datos_num= [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
print(datos_num)
print("-----------")
for a in datos_num:
        for b in a:
         if a[0]==0:
          datos_num.remove(a)
       
         if b==0:
          a.remove(b)
                   
print(datos_num)
print(a)
        
        
        
       
           
    
    
   
        
    

            
        
            
           
          
       
        
