import pandas as pd

# 1. Leer el archivo CSV
# Se recomienda especificar el parámetro 'skipinitialspace=True' para eliminar espacios después de las comas
raw_df = pd.read_csv("SalesJan20091.csv", skipinitialspace=True)
print("1. Datos originales (primeras filas):")
print(raw_df.head(), "\n")

# 2. Eliminar espacios en los nombres de las columnas
raw_df.columns = raw_df.columns.str.strip()
print("2. Nombres de columnas después de eliminar espacios:")
print(raw_df.columns, "\n")

# 3. Eliminar espacios al inicio y final de los valores tipo string en todo el DataFrame
def strip_strings(df):
    for col in df.select_dtypes(include=["object"]):
        df[col] = df[col].str.strip()
    return df
clean_df = strip_strings(raw_df)
print("3. Ejemplo de filas tras eliminar espacios en los valores string:")
print(clean_df.head(), "\n")

# 4. Convertir columnas a los tipos de datos correctos
# Por ejemplo, convertir fechas y precios
def convert_types(df):
    df["Transaction_date"] = pd.to_datetime(df["Transaction_date"], errors="coerce")
    df["Account_Created"] = pd.to_datetime(df["Account_Created"], errors="coerce")
    df["Last_Login"] = pd.to_datetime(df["Last_Login"], errors="coerce")
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
    df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
    return df
clean_df = convert_types(clean_df)
print("4. Tipos de datos después de la conversión:")
print(clean_df.dtypes, "\n")

# 5. Eliminar filas duplicadas
clean_df = clean_df.drop_duplicates()
print("5. Número de filas después de eliminar duplicados:", len(clean_df), "\n")

# 6. Manejar valores faltantes (NaN)
# Ejemplo: mostrar cuántos valores faltantes hay por columna
print("6. Valores faltantes por columna:")
print(clean_df.isnull().sum(), "\n")

# Ejemplo de cómo rellenar valores faltantes en la columna 'State' con 'Desconocido'
clean_df["State"] = clean_df["State"].fillna("Desconocido")

# 7. Estandarizar el texto (por ejemplo, mayúsculas/minúsculas en países)
clean_df["Country"] = clean_df["Country"].str.title()
print("7. Ejemplo de estandarización de texto en 'Country':")
print(clean_df["Country"].unique(), "\n")

# 8. Validar rangos de valores (ejemplo: precios positivos)
invalid_prices = clean_df[clean_df["Price"] <= 0]
print("8. Filas con precios no válidos (<=0):")
print(invalid_prices, "\n")

# 9. Guardar el DataFrame limpio a un nuevo archivo CSV
clean_df.to_csv("SalesJan20091_clean.csv", index=False)
print("9. Archivo limpio guardado como 'SalesJan20091_clean.csv'") 