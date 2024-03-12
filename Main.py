import streamlit as st
import requests 
import asyncio


st.set_page_config(layout='wide') #Configuracion de la pagina 
st.title('Consumo de APIS') # titulo
st.divider() # Divisor 
#Instrucciones de uso
st.caption('Seleccione la API que desea utilizar en dando click en la tab correspondiente. '
           'Modifique los parametros del modo que desee y la query se ejecutara automaticamente.')
async def query_image(quantity=1,typ='kittens',height=300):
    """
    Hace una peticion get a la API de imagenes de https://fakerapi.it/ 
    y retorna la respuesta de la petición.

    Args:
        quantity (int, optional): Cantidad de imagenes a consultar. Defaults to 1.
        typ (str, optional): tipo de images a consultar. Defaults to 'kittens'.
        height (int, optional): largo de la imagen en pixeles. Defaults to 300.

    Returns:
        dict : respuesta de la request
    """
    # Hacemos la peticion get al servidor especificando los parametros de la query (cantidad,altura y tipo de imagenes)
    data = await asyncio.to_thread(requests.get,f'https://fakerapi.it/api/v1/images?_quantity={quantity}&_type={typ}&_height={height}')
    return data.json() #Retornamos los datos


async def query_text(chars=500, quantity=1):
    """
    Hace una peticion get a la API de imagenes de https://fakerapi.it/ 
    y retorna la respuesta de la petición.
    Args:
        chars (int, optional): Cantidad de caracteres en el texto. Defaults to 500.
        quantity (int, optional): Cantidad de textos a consultar. Defaults to 1.

    Returns:
        dict: respuesta de la request
    """
    data = await asyncio.to_thread(requests.get,f'https://fakerapi.it/api/v1/texts?_quantity={quantity}&_characters={chars}')
    return data.json()


async def query_users(gender='male', quantity=1):
    data = await asyncio.to_thread(requests.get,f'https://fakerapi.it/api/v1/users?_quantity={quantity}&_gender={gender}')
    return data.json()


#las tabs nos ayudan a organizar las diferentes apis por tabs
tabs = st.tabs(['API Imagenes','API Textos','API Usuarios'])

#Interfaz grafica para leer los parametros de la query
with tabs[0]:
    #Contenido de la primer tab
    st.header('API Imagenes') #Titulo
    typ = st.text_input('Ingrese el tipo de imagen',placeholder='dogs',value='dogs') # Entrada de texto
    c1,c2 = st.columns(2) #Sirve para poner dos entradas en una misma fila 
    height = c1.number_input('Ingrese la altura de la imagen',min_value=100, max_value=900,value=300) # Entrada Enteros
    quantity = c2.number_input('Ingrese la cantidad de imagenes', min_value=1,max_value=10) # Entrada Enteros
    st.write(':blue[Respuesta RAW:]')
    with st.spinner(): # Nos ayuda a desplegar un icono de cargando mientras se procesa la request
        response1 = asyncio.run(query_image(typ=typ,quantity=quantity,height=height)) # Llamamos a la funcion que se ejecuta de manera asincrona
    st.json(response1) #Imprimimos el resultado de la query


#Analogo
with tabs[1]:
    #contenido de la segunda tab
    st.header('API Textos')
    quantitytexts = st.number_input('Cantidad de textos a consultar',min_value=1,max_value=10)
    lenchars = st.number_input('Numero de caracteres en el texto',min_value=100,max_value=5000,value=500)
    st.write(':blue[Respuesta RAW:]')
    with st.spinner():
        response2 = asyncio.run(query_text(lenchars,quantitytexts))
    st.json(response2)

#Analogo 
with tabs[2]:
    #contenido de la segunda tab
    st.header('API Usuarios')
    quantityusers = st.number_input('Cantidad de usuarios a consultar',min_value=1,max_value=10)
    gender = st.selectbox('Genero de los usuarios',['male','female'])
    st.write(':blue[Respuesta RAW:]')
    with st.spinner():
        response3 = asyncio.run(query_users(gender,quantityusers))
    st.json(response3)