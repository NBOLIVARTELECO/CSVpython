# Proyecto: Manejo y Limpieza de Datos CSV en Python

## Archivos contenidos

- **SalesJan20091.csv**
  - Archivo de datos original en formato CSV. Contiene información de ventas, incluyendo fecha de transacción, producto, precio, tipo de pago, nombre del cliente, ciudad, estado, país, fechas de cuenta y login, latitud y longitud.

- **csv_app.py**
  - Script principal de análisis y visualización de datos. Permite generar diferentes reportes y gráficos a partir del archivo CSV, como ventas por fecha, producto, país, tipo de pago, y más. Incluye funciones para cada análisis y puedes activarlas/desactivarlas desde el bloque `if __name__ == "__main__":`.

- **data_cleaning_example.py**
  - Ejemplo detallado de limpieza y homogeneización de datos. Explica paso a paso cómo eliminar espacios, convertir tipos de datos, manejar valores faltantes, eliminar duplicados, estandarizar texto y validar rangos. Al final, guarda un archivo limpio llamado `SalesJan20091_clean.csv`.

- **SalesJan20091_clean.csv**
  - Archivo generado por el script de limpieza, contiene los datos originales pero ya procesados y limpios.

## Requisitos

- Python 3.x
- pandas
- matplotlib

Instala las dependencias con:
```sh
pip install pandas matplotlib
```

## Uso

1. **Limpieza de datos:**
   - Ejecuta `data_cleaning_example.py` para limpiar y homogeneizar el archivo CSV original.
   - Se generará un archivo limpio `SalesJan20091_clean.csv`.

2. **Análisis y visualización:**
   - Ejecuta `csv_app.py` para ver ejemplos de análisis y gráficos sobre los datos.
   - Puedes activar/desactivar los análisis que desees desde el bloque principal del script.

---

Si tienes dudas sobre algún paso o necesitas agregar nuevas funciones, ¡no dudes en consultar o modificar los scripts! 