import streamlit as st

# Diccionario con las categorías y sus respectivas conversiones
conversiones = {
    "Temperatura": {
        "Celsius a Fahrenheit": lambda c: c * 9/5 + 32,
        "Fahrenheit a Celsius": lambda f: (f - 32) * 5/9,
        "Celsius a Kelvin": lambda c: c + 273.15,
        "Kelvin a Celsius": lambda k: k - 273.15
    },
    "Longitud": {
        "Pies a Metros": lambda ft: ft * 0.3048,
        "Metros a Pies": lambda m: m / 0.3048,
        "Pulgadas a Centímetros": lambda inch: inch * 2.54,
        "Centímetros a Pulgadas": lambda cm: cm / 2.54
    },
    "Peso/Masa": {
        "Libras a Kilogramos": lambda lb: lb * 0.453592,
        "Kilogramos a Libras": lambda kg: kg / 0.453592,
        "Onzas a Gramos": lambda oz: oz * 28.3495,
        "Gramos a Onzas": lambda g: g / 28.3495
    },
    "Volumen": {
        "Galones a Litros": lambda gal: gal * 3.78541,
        "Litros a Galones": lambda l: l / 3.78541,
        "Pulgadas cúbicas a Centímetros cúbicos": lambda inch3: inch3 * 16.3871,
        "Centímetros cúbicos a Pulgadas cúbicas": lambda cm3: cm3 / 16.3871
    },
    "Tiempo": {
        "Horas a Minutos": lambda hr: hr * 60,
        "Minutos a Segundos": lambda min: min * 60,
        "Días a Horas": lambda day: day * 24,
        "Semanas a Días": lambda week: week * 7
    },
    "Velocidad": {
        "Millas por hora a Kilómetros por hora": lambda mph: mph * 1.60934,
        "Kilómetros por hora a Metros por segundo": lambda kph: kph * 0.277778,
        "Nudos a Millas por hora": lambda knot: knot * 1.15078,
        "Metros por segundo a Pies por segundo": lambda mps: mps * 3.28084
    },
    "Área": {
        "Metros cuadrados a Pies cuadrados": lambda sqm: sqm * 10.7639,
        "Pies cuadrados a Metros cuadrados": lambda sqft: sqft / 10.7639,
        "Kilómetros cuadrados a Millas cuadradas": lambda sqkm: sqkm * 0.386102,
        "Millas cuadradas a Kilómetros cuadrados": lambda sqmi: sqmi / 0.386102
    },
    "Energía": {
        "Julios a Calorías": lambda j: j * 0.239006,
        "Calorías a Kilojulios": lambda cal: cal * 4.184,
        "Kilovatios-hora a Megajulios": lambda kwh: kwh * 3.6,
        "Megajulios a Kilovatios-hora": lambda mj: mj / 3.6
    },
    "Presión": {
        "Pascales a Atmósferas": lambda pa: pa * 0.00000986923,
        "Atmósferas a Pascales": lambda atm: atm * 101325,
        "Barras a Libras por pulgada cuadrada": lambda bar: bar * 14.5038,
        "Libras por pulgada cuadrada a Barras": lambda psi: psi / 14.5038
    },
    "Tamaño de datos": {
        "Megabytes a Gigabytes": lambda mb: mb / 1024,
        "Gigabytes a Terabytes": lambda gb: gb / 1024,
        "Kilobytes a Megabytes": lambda kb: kb / 1024,
        "Terabytes a Petabytes": lambda tb: tb / 1024
    }
}

# Configuración de la aplicación
st.title("Conversor Universal")
categoria = st.selectbox("Seleccione una categoría", list(conversiones.keys()))

# Convertir unidad
if categoria:
    conversion = st.selectbox(f"Seleccione una conversión de {categoria}", list(conversiones[categoria].keys()))
    valor = st.number_input(f"Ingrese el valor en {conversion.split(' a ')[0]}")
    resultado = conversiones[categoria][conversion](valor)
    st.write(f"El resultado es: {resultado} {conversion.split(' a ')[1]}")
