# 🗞️ News Aggregator – Multi-Scraper de Noticias

Proyecto desarrollado con Scrapy para la agregación de noticias desde múltiples fuentes en un único formato de datos unificado.

### 📌 Objetivo del proyecto

El objetivo de este proyecto es construir un multi-scraper de noticias capaz de extraer información relevante desde tres medios de comunicación distintos, normalizar los datos y exportarlos a un solo archivo JSON.

Este proyecto demuestra:

- Uso de múltiples spiders en Scrapy

- Extracción de datos con CSS Selectors y XPath

- Limpieza y normalización de datos

- Exportación de resultados a un formato común

---


# 🕷️ Spiders implementados

El proyecto contiene tres spiders independientes, cada uno enfocado en una fuente distinta:

### 1️⃣ Spider con CSS Selectors

Extrae noticias del periódico El Pais utilizando solo selectores CSS

Obtiene:

- Fuente

- Título

- Fecha

- Autor

- Noticia

Limpia espacios en blanco y saltos de línea

### 2️⃣ Spider con XPath

Utiliza únicamente expresiones XPath

Extrae noticias del periódico La Voz de Galicia utilizando solo selectores XPath

Obtiene:

- Fuente

- Título

- Autor

- Noticia

- Dato

### 3️⃣ Spider libre

Utiliza únicamente expresiones XPath

Extrae noticias del periódico Marca utilizando solo selectores XPath

Obtiene:

- Fuente

- Título

- Autor

- Noticia

- Dato

---

# ▶️ Ejecución del proyecto

Cada spider puede ejecutarse de forma individual y exportar los resultados a un único archivo JSON.

---

# 📦 Archivo de salida

El archivo salidas.json:

- Contiene todas las noticias extraídas

- Usa un formato unificado

- Está incluido directamente en el repositorio
