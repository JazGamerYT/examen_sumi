# Usar una imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias 'requirements.txt' al contenedor
COPY requirements.txt requirements.txt

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que Flask correrá (por defecto, Flask usa el puerto 5000)
EXPOSE 5000

# Definir el comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
