import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
ventasdf = pd.read_csv("SalesJan20091.csv")

# 1. Mostrar las primeras filas del archivo
print("1. Primeras filas del archivo:")
print(ventasdf.head(), "\n")

# 2. Convertir la columna de fecha a tipo datetime
ventasdf["Transaction_date"] = pd.to_datetime(ventasdf["Transaction_date"])

# 3. Reporte de ventas por fecha (gráfico)
print("2. Gráfico de ventas por fecha:")
A = (ventasdf["Transaction_date"]
     .dt.floor("d")
     .value_counts()
     .rename_axis("date")
     .reset_index(name="num ventas"))
A = A.sort_values("date")
A.plot(x="date", y="num ventas", color="green", title="Ventas por fecha")
plt.show()

# 4. Ventas totales por producto
print("3. Ventas totales por producto:")
ventas_producto = ventasdf["Product"].value_counts()
print(ventas_producto, "\n")

# 5. Ingresos totales por producto
print("4. Ingresos totales por producto:")
ingresos_producto = ventasdf.groupby("Product")["Price"].sum()
print(ingresos_producto, "\n")

# 6. Ventas por tipo de pago
print("5. Ventas por tipo de pago:")
ventas_pago = ventasdf["Payment_Type"].value_counts()
print(ventas_pago, "\n")

# 7. Ventas por país
print("6. Ventas por país:")
ventas_pais = ventasdf["Country"].value_counts()
print(ventas_pais, "\n")

# 8. Ingresos totales por país
print("7. Ingresos totales por país:")
ingresos_pais = ventasdf.groupby("Country")["Price"].sum()
print(ingresos_pais, "\n")

# 9. Filtrar ventas mayores a $1000
print("8. Ventas mayores a $1000:")
ventas_mayores_1000 = ventasdf[ventasdf["Price"] > 1000]
print(ventas_mayores_1000, "\n")

# 10. Obtener la venta más cara
print("9. Venta más cara:")
venta_mas_cara = ventasdf.loc[ventasdf["Price"].idxmax()]
print(venta_mas_cara, "\n")

# 11. Gráfico de ventas por ciudad (top 10)
print("10. Gráfico de ventas por ciudad (top 10):")
ventas_ciudad = ventasdf["City"].value_counts().head(10)
ventas_ciudad.plot(kind="bar", title="Top 10 ciudades con más ventas")
plt.show() 