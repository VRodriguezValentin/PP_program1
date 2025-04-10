# 🚗 Sistema de Gestión de Estacionamientos

Proyecto para gestionar múltiples estacionamientos con registro de ingresos, egresos, recaudaciones, y más.

---

## 🧾 Funcionalidades Principales

- Alta de estacionamientos
- Ingreso y egreso de vehículos
- Control de parcelas disponibles
- Modificación de tarifas por hora
- Reportes y listados inteligentes con `map()`, `filter()` y `reduce()`
- Exportación a JSON y registro en TXT

---

## 📋 Enunciado / Funciones

### 1️⃣ Nuevo Estacionamiento

- Alta con ID (nombre único)
- Validación: nombre único, tarifas como `float > 0`, parcelas como `int > 0`
- Estructura:
```python
[{'objeto': Vehículo, 'hora_ingreso': HH:MM}, {...}]
```

### 2️⃣ Ingreso de Vehículo

- Selección de estacionamiento
- Creación de objeto `Vehículo` con patente y tipo
- Se descuenta una parcela disponible
- Se registra `hora_ingreso`

### 3️⃣ Egreso de Vehículo

- Se selecciona el vehículo en lista
- Se libera la parcela
- Se calcula tiempo total usando `datetime`
- Se calcula importe a pagar

### 4️⃣ Modificar Costes por Hora

- Se permite modificar:
  - `coste_hora_auto`
  - `coste_hora_moto`
- Validación: flotantes positivos

### 5️⃣ Listar Vehículos Estacionados

- Utiliza `map()` para aplicar función a cada vehículo
- Muestra datos como patente, tipo, y hora de ingreso

### 6️⃣ Ordenar Vehículos por Patente

- Ordena de forma **descendente** las patentes estacionadas por establecimiento

---

## 💰 Recaudación y Reportes Avanzados

### 7️⃣ Recaudación Total

- Usa `reduce()` para sumar la recaudación de **todos los estacionamientos**

### 8️⃣ Vehículos +60 min

- Usa `filter()` para mostrar solo los vehículos con tiempo > 60 min estacionados

### 9️⃣ Guardar en JSON

- Toda la estructura de estacionamientos se guarda en:
```
db_estacionamientos.json
```
- Al iniciar el programa, se debe cargar la data desde ese archivo

### 🔟 Ver Log de Ingresos/Egresos

- Registro de actividad en archivo `log_estacionamientos.txt`

#### Formato Ingreso:
```
[Patente: XXX-NNN] [Hora ingreso: DD-MM-YYYY HH:MM]
```

#### Formato Egreso:
```
[Patente: XXX-NNN] [Hora ingreso: DD-MM-YYYY HH:MM] [Hora egreso: DD-MM-YYYY HH:MM] [Importe]
```

---

## 🎓 Condiciones de Aprobación

| Nota | Requisitos |
|------|------------|
| 4    | Punto 1 al 6 |
| 6+   | Punto 7 al 10 |

---

## 🧪 Requisitos Técnicos

- Python 3.10+
- Uso de funciones de orden superior (`map`, `filter`, `reduce`)
- Manejo de archivos JSON y TXT
- Validaciones y estructura orientada a objetos

---

## 🏁 ¡Manos a la obra!

Este sistema puede ser fácilmente extendido con interfaces gráficas, base de datos relacional o conexión en red.

---
