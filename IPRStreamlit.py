#Libreras a importar
import streamlit as st
import pandas as pd
import math
import altair as alt
from PIL import Image

image1 = Image.open('Image1.jpg')
image2 = Image.open('formulas.PNG')
html_temp = """
	<div style="background-color:teal ;padding:10px">
	<h2 style="color:white;text-align:center;">IPR para un sistema radial - Ecuación de difusividad Estado semiestable</h2>
	</div>
	"""

st.markdown(html_temp, unsafe_allow_html=True)



st.sidebar.title('IPR (Inflow Performance Relationship)')
st.sidebar.image(image1, caption='Ing. Carlos Carrillo - App version 0.1',
          use_column_width=True)

st.sidebar.subheader('Parámetros')
# Parámetros en slidebar
def parametros_ipr():
	
	permeabilidad = st.sidebar.slider('Permeabilidad K [md]', 0 , 100 , 30,  step = 1 )
	espesor = st.sidebar.slider('Espesor h [ft]', 0,100 , 40 , step=1)
	presion_yacimiento = st.sidebar.slider('Presión de yacimiento Pr [PSI]',0,10000,3000, step= 100)
	presion_fondo_fluyenye = st.sidebar.slider('Presión de fondo fluyente Pwf [PSI]',0,10000,2400, step= 100)
	viscosidad = st.sidebar.slider('Viscosidad [cP] ', 0.000, 10.000 , 0.959 , step = 0.01)
	factor_volumetrico_oil = st.sidebar.slider('Factor volumétrico Oil [BY/BN]', 0.01,3.00 , 1.187 , step=0.01)
	radio_yacimiento = st.sidebar.slider('Radio del yacimiento [ft]',1000,10000,1507, step= 100)
	skin = st.sidebar.slider('Skin',-15.0,15.0,10.0, step= 0.1)
	
	st.sidebar.subheader('Diametro del pozo [In]')

	selectbox1 = st.sidebar.selectbox(
    	"Parte Entera",
    	("4","5","6", "7", "8","9","10" ,"11","12","13" ,"18", "20","22","24","26","30","36","40","42"), index=8)

	if selectbox1 == '4':
		parte_entera = 4
	if selectbox1 == '5':
		parte_entera = 5
	if selectbox1 == '6':
		parte_entera = 6
	if selectbox1 == '7':
		parte_entera = 7
	if selectbox1 == '8':
		parte_entera = 8
	if selectbox1 == '9':
		parte_entera = 9
	if selectbox1 == '10':
		parte_entera = 10
	if selectbox1 == '11':
		parte_entera = 11
	if selectbox1 == '12':
		parte_entera = 12
	if selectbox1 == '13':
		parte_entera = 13
	if selectbox1 == '18':
		parte_entera = 18
	if selectbox1 == '20':
		parte_entera = 20
	if selectbox1 == '22':
		parte_entera = 22
	if selectbox1 == '24':
		parte_entera = 24
	if selectbox1 == '26':
		parte_entera = 26
	if selectbox1 == '30':
		parte_entera = 30
	if selectbox1 == '36':
		parte_entera = 36
	if selectbox1 == '40':
		parte_entera = 40
	if selectbox1 == '42':
		parte_entera = 42

	selectbox2 = st.sidebar.selectbox(
    	"Parte decimal",
    	("0", "1/4" ,"1/2" , "5/8" , "3/4" , "3/8" , "7/8"  ), index=1)
	if selectbox2 == '0':
		parte_decimal = 0
	if selectbox2 == '1/4':
		parte_decimal = 0.25
	if selectbox2 == '1/2':
		parte_decimal = 0.5
	if selectbox2 == '5/8':
		parte_decimal = 0.625
	if selectbox2 == '3/4':
		parte_decimal = 0.75
	if selectbox2 == '3/8':
		parte_decimal = 0.375
	if selectbox2 == '7/8':
		parte_decimal = 0.875


	permeabilidad = round(permeabilidad,2)
	espesor = round(espesor,2)
	presion_yacimiento = round(presion_yacimiento,2)
	presion_fondo_fluyenye = round(presion_fondo_fluyenye,2)
	viscosidad = round(viscosidad,3)
	factor_volumetrico_oil = round(factor_volumetrico_oil,3)
	radio_yacimiento = round(radio_yacimiento,2)
	skin =round(skin,2)


	data_inicial  =	{'Permeabilidad K [md]': permeabilidad,
					 'Espesor h [ft]': espesor,
					 'Presión de yacimiento Pr [PSI]': presion_yacimiento,
			 		 'Presión de fondo fluyente Pwf [PSI]': presion_fondo_fluyenye,
			 		 'Viscosidad [cP]': viscosidad,
			 		 'Factor volumétrico Oil [BY/BN]': factor_volumetrico_oil,
			 		 'Radio del yacimiento [ft]': radio_yacimiento,
			 		 'Diametro  del pozo[In]':parte_entera+parte_decimal,
			 		 'Radio del pozo [ft]': (parte_entera+parte_decimal)/24,
			 		 'Skin': skin,
			 		 }
		

	parametros_iniciales = pd.DataFrame(data_inicial, index=['-'])
	return parametros_iniciales

df_parametros_ipr = parametros_ipr()
st.subheader('Parámetros')
st.write(df_parametros_ipr.T)

var_permeabilidad = df_parametros_ipr.loc['-' ,'Permeabilidad K [md]']
var_espesor = df_parametros_ipr.loc['-' ,'Espesor h [ft]']
var_presion_yacimiento = df_parametros_ipr.loc['-' ,'Presión de yacimiento Pr [PSI]']
var_presion_fondo_fluyenye = df_parametros_ipr.loc['-' ,'Presión de fondo fluyente Pwf [PSI]']
var_viscosidad = df_parametros_ipr.loc['-' ,'Viscosidad [cP]']
var_factor_volumetrico_oil = df_parametros_ipr.loc['-' ,'Factor volumétrico Oil [BY/BN]']
var_radio_yacimiento = df_parametros_ipr.loc['-' ,'Radio del yacimiento [ft]']
var_radio_pozo = df_parametros_ipr.loc['-' ,'Radio del pozo [ft]']
var_skin = df_parametros_ipr.loc['-' ,'Skin']

tasa_produccion_pwf = (0.00708*var_permeabilidad*var_espesor*(var_presion_yacimiento - var_presion_fondo_fluyenye))/(var_viscosidad*var_factor_volumetrico_oil*(math.log(var_radio_yacimiento/var_radio_pozo)-0.75+var_skin))
indice = tasa_produccion_pwf/(var_presion_yacimiento - var_presion_fondo_fluyenye)
indice = round(indice,3)
if indice < 0.5 :
	Resultado_indice = 'Baja productividad'
if indice > 0.5 and indice < 1 :
	Resultado_indice = 'Productividad media'
if indice > 1 and indice < 2 :
	Resultado_indice = 'Alta productividad'
if indice > 2 :
	Resultado_indice = 'Excelente productividad'

qmax=var_presion_yacimiento*indice





lista_q = [0,(qmax*1/10),(qmax*2/10),(qmax*3/10),(qmax*4/10),(qmax*5/10),(qmax*6/10),(qmax*7/10),(qmax*8/10),(qmax*9/10),(qmax*10/10)]
lista_pfw = [ var_presion_yacimiento-(n/indice) for n in lista_q]

data_ipr = {'Caudal BPD':lista_q,
			'Presión PSI':lista_pfw }

df_data_ipr =pd.DataFrame(data_ipr).astype('int')
df_data_ipr2 =pd.DataFrame(data_ipr)

check_IPR_formulas = st.checkbox('Fórmulas', value=False, key=None)
	
if check_IPR_formulas  == True:
	st.image(image2, caption='Esquema y formulas empleadas',
          use_column_width=True)

#******************************************************************************************************
selectbox_calculos=st.selectbox(
    "Cálculos preliminares de yacimiento",
    ( "Datos disponibles","Calcular Datos"), index=0)

if 	selectbox_calculos == 'Calcular Datos':
	st.subheader("Bo, Rs, po y uo , para petróleo saturado (P < ó = Pb)")
	api = st.slider('API del petróleo', 0.0 , 100.0 , 30.0,  step = 0.1 )
	gravedad_especifica_gas =st.slider('Gravedad especifica del gas', 0.0 , 1.0, 0.7,  step = 0.01 )
	presion_de_burbuja =st.slider('Presión de burbuja', 0, 10000,1814, step= 1)
	temperatura_yacimiento  = st.slider('Temperatura del yacimiento', 0 , 400,200, step = 1)
	gravedad_especifica_oil = (141.5)/(131.5+api)

	st.subheader('Relación de solubilidad por Standing')

	Rs = gravedad_especifica_gas*(((presion_de_burbuja/18.2)+1.4)*10**((0.0125*api)-(0.00091*temperatura_yacimiento)))**1.2048
	Rs = round(Rs,0)
	st.write('Rs',Rs)

	st.subheader('Bo y Uo a la presión de burbuja')

	Bo = 0.9759 +0.00012*((Rs*(gravedad_especifica_gas/gravedad_especifica_oil)**0.5)+(1.25*temperatura_yacimiento))**1.2
	Bo = round(Bo,4)
	st.write('Bo:',Bo)


	uod = 10**((10**(3.0324-0.02023*api))*(temperatura_yacimiento**-1.163))    -1
	uod = round(uod,4)
	st.write('Uod:',uod)

	a = 10.715*(Rs+100)**-0.515
	b = 5.44*(Rs+150)**-0.338
	uo = a*(uod)**b
	uo = round(uo,4)
	st.write('Uo:',uo)

	st.subheader('Bo y Uo a la presion estática del yacimiento (Presión mayor a Presión de burbuja)')
	Bo2 = Bo*2.7182818284590452353602874713527**(-0.0000151*(var_presion_yacimiento - presion_de_burbuja))
	Bo2 = round(Bo2,4)
	st.write('Bo:',Bo2)
	uo2 = 1.0008*uo + 0.001127*(var_presion_yacimiento - presion_de_burbuja)*(0.038*(uo)**1.59 - 0.006517*(uo)**1.8148)
	uo2 = round(uo2,2)
	st.write('Uo:',uo2)

	st.subheader('Bo y Uo  promedio')
	uom = (uo + uo2)/2
	Bom = (Bo + Bo2)/2
	uom = round(uom,3)
	Bom = round(Bom,3)
	st.subheader('Estos resultados ingresar en el slidebar')
	st.write('Ingresar en el slidebar: Factor volumétrico Oil [BY/BN]')
	st.write('Bo:',Bom)
	st.write('Ingresar en el slidebar: Viscosidad [cP]')
	st.write('Uo:',uom)
#******************************************************************************************************

check_IPR = st.checkbox('Cálculos IPR', value=False, key=None)
	
if check_IPR == True:

	st.subheader('Tasa de producción en Pwf')
	st.write('Q:',tasa_produccion_pwf)
	st.subheader('Índice de productividad J ')
	st.write('J:',indice)
	st.write('Resultado del indice J:',Resultado_indice)
	

	st.write(df_data_ipr)



	nearest = alt.selection(type='single', nearest=True, on='mouseover',
			                        fields=['Caudal BPD'], empty='none')
			
	grafico_lineas = alt.Chart(df_data_ipr).mark_line(color = 'red').encode(
			    x='Caudal BPD',
			    y='Presión PSI',
			    tooltip=['Caudal BPD','Presión PSI']
			    
			)

	selectors = alt.Chart(df_data_ipr).mark_point().encode(
			    x='Caudal BPD',
			    opacity=alt.value(0),
			).add_selection(
			    nearest
			)
	points = grafico_lineas.mark_point().encode(
			    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
			)

	text = grafico_lineas.mark_text(align='left', dx=5, dy=-5).encode(
			    text=alt.condition(nearest, 'Presión PSI', alt.value(' '))
			)

	rules = alt.Chart(df_data_ipr).mark_rule(color='gray').encode(
			    x='Caudal BPD',
			).transform_filter(
			    nearest
			)

	grafico_capas = alt.layer( grafico_lineas, selectors, points,  rules , text).properties( width=600, height=300).interactive()

	st.altair_chart(grafico_capas)






