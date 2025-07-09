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

def plot_sales_by_date():

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
def plot_sales_by_product():
     print("3. Ventas totales por producto:")
     ventas_producto = ventasdf["Product"].value_counts()
     print(ventas_producto, "\n")
     ventas_producto.plot(kind="bar", title="Ventas por producto")
     plt.show()

# 5. Ingresos totales por producto
def plot_revenue_by_product():
     print("4. Ingresos totales por producto:")
     ingresos_producto = ventasdf.groupby("Product")["Price"].sum()
     print(ingresos_producto, "\n")
     ingresos_producto.plot(kind="bar", title="ingresos por producto")
     plt.show()

# 6. Ventas por tipo de pago
def plot_sales_by_payment_type():
     print("5. Ventas por tipo de pago:")
     ventas_pago = ventasdf["Payment_Type"].value_counts()
     print(ventas_pago, "\n")
     ventas_pago.plot(kind="bar", title="Ventas por tipo de pago")
     plt.show()

# 7. Ventas por país
def plot_sales_by_country():
     print("6. Ventas por país:")
     ventas_pais = ventasdf["Country"].value_counts()
     print(ventas_pais, "\n")
     ventas_pais.plot(kind="bar", title="Ventas por país")
     plt.show()

# 8. Ingresos totales por país
def plot_revenue_by_country():
     print("7. Ingresos totales por país:")
     ingresos_pais = ventasdf.groupby("Country")["Price"].sum()
     print(ingresos_pais, "\n")

# 9. Filtrar ventas mayores a $1000
def filter_sales_above_1000():
     print("8. Ventas mayores a $1000:")
     ventas_mayores_1000 = ventasdf[ventasdf["Price"] > 1000]
     print(ventas_mayores_1000, "\n")

# 10. Obtener la venta más cara
def get_most_expensive_sale():     
     print("9. Venta más cara:")
     venta_mas_cara = ventasdf.loc[ventasdf["Price"].idxmax()]
     print(venta_mas_cara, "\n")

# 11. Gráfico de ventas por ciudad (top 10)
def plot_sales_by_city():
     print("10. Gráfico de ventas por ciudad (top 10):")
     ventas_ciudad = ventasdf["City"].value_counts().head(10)
     print(type(ventas_ciudad), "\n")
     ventas_ciudad.plot(kind="bar", title="Top 10 ciudades con más ventas")
     plt.show() 

# Ejecutar las funciones
if __name__ == "__main__":
     #plot_sales_by_date()
     #plot_revenue_by_product()
     #plot_sales_by_product()
     #plot_sales_by_payment_type()
     #plot_sales_by_country()
     #plot_revenue_by_country()
     #filter_sales_above_1000()
     #get_most_expensive_sale()
     plot_sales_by_city()