#!/usr/bin/env python
# coding: utf-8

# In[24]:


get_ipython().system('pip install pandas')


# In[3]:


import pandas as pd        
from string import ascii_uppercase as alfabeto
import pickle


#-utilizamos pandas para hacer lectura del Html de la pagina mediante el metodo pd.read_html
#-imporrtamos el alfabeto para hacer un pequeño proceso de etl que es darle nombre acada llave
#y con la libreria pickle haremos uso del metodo ouput para exportar nuestro diccionario


# In[4]:


grupos = pd.read_html('https://es.wikipedia.org/wiki/Copa_Libertadores_2023')
grupos
#usamos el metodo pd.read_html. a la url que necesitamos scrapear, cabe destacar que este metodo solo es eficiente 
#cuando la pagina es puramente HTML como es el caso de wikipedia


# In[5]:


#hacemos busqueda de la informacion que necesitamos extraer, en mi caso empezaba con la tabla de grupo 19

grupos[19]



# In[6]:


grupos[40].columns[0]

#probamos si la lectura es correcta mediante el llamado a la llave de grupo que nececitamos y le agregamos la consulta a la columna 

#asu vez calculamos el intervalo de aparacion entre llaves,para ver si exite o no un patron de diceño en el html
grupos[19]
grupos[22]
#.....      #patron detectado: diferecias de 3 en 3
rupos[40]
grupos[43]


# In[7]:


grupos = pd.read_html('https://es.wikipedia.org/wiki/Copa_Libertadores_2023')
for i in range(19, 43, 3):
    df= grupos[i]
    print(df) 
#mediante bucle for in range iteramos de forma especifica en un rango determinado, en mi caso da comienzo en el elmento 19,
#va hasta el 43 pero no lo incluye y se separa de 3 en 3 



# In[8]:


for letra, i in zip(alfabeto, range (19, 43, 3)):
    print(letra, i)
    
    
#en este proceso de etl, vamos a asignarle una letra a cada llave de grupo, esto nos facilitara el llamdo a cada llave cuando lo necesitemos
#en este codigo hacemos la prueba de si el bucle con doble variable condicionado por el rango nos permite grabar cada letra a cada numero de tabla


# In[9]:


grupos = pd.read_html('https://es.wikipedia.org/wiki/Copa_Libertadores_2023')
diccionario_grupos={}
for letra, i in zip(alfabeto, range(19, 43, 3)):
    df= grupos[i]
    diccionario_grupos[f'Grupo {letra}'] = df
    
#aca resumo todos los pasos anteriores en solo un fragmento de codigo.


# In[10]:


diccionario_grupos.keys()


# In[11]:


grupo_a = diccionario_grupos.get('Grupo A')
if grupo_a is not None:
    print(grupo_a)
else:
    print("La clave 'Grupo A' no existe en el diccionario.")
#Este codigo es util para determinar si el paso anterior es correcto


# In[12]:


diccionario_grupos['Grupo D']   #pruebo la consulta mediante el nombre de cada grupo


# In[13]:


diccionario_grupos   #hacemos consulta al diccionario para ver su contenido y diseño.


# In[22]:


import pickle

with open('diccionario_grupos', 'wb') as output:
    pickle.dump(diccionario_grupos, output)
#serializamos la informacion y exportamos el diccionario con la instrucion with y la funcion Open a la salida output


# In[25]:


#si tienen problemas para la posterior lectura del archivo exportado podemos consultar mediante Chardet
#la codificacion de dicho archivo binario, sera dependiente del so que esten utilizando
#para resolver error del codigo anterior

import chardet

with open('diccionario_grupos', 'rb') as f:
    result = chardet.detect(f.read())
print(result['encoding'])


# In[ ]:


#para resolver error del codigo anterior o bien darle el codificado que necesitemos.

with open('diccionario_grupos', 'wb', encoding='Windows-1254') as output:
    pickle.dump(diccionario_grupos, output)
    


# In[ ]:




