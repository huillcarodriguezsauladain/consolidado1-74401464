# Práctica Calificada - Consolidado 1
## Construcción de Software (ASUC00947) - Ciclo VII (2026-20)

- **Estudiante:** SAUL ADAIN HUILLCA RODRIGUEZ
- **Código de alumno:** 74401464
- **Carrera:** Ingeniería de Sistemas e Informática
- **Universidad:** Universidad Continental

---

### Descripción del Proyecto
Este repositorio contiene el desarrollo completo de la Práctica Calificada - Consolidado 1 correspondiente al curso de Construcción de Software. Se implementan ejercicios de Programación Orientada a Objetos (POO) en Python y se demuestra el flujo de trabajo colaborativo siguiendo la metodología Gitflow, incluyendo el uso de Conventional Commits, ramas feature, integración mediante merge sin avance rápido (`--no-ff`), y el ciclo completo de atención de una rama `hotfix`.

### Estructura y Archivos del Repositorio
El proyecto está estructurado modularmente con los siguientes archivos en la raíz del repositorio:

1. **`planeta.py`**:
   - Implementa la clase `Planeta` con atributos de instancia: `nombre`, `masa`, `radio`, `distancia_al_sol` y `tiene_vida` (por defecto `False`).
   - Método `calcular_densidad()`: Calcula la densidad media en kg/m³ aplicando la fórmula física del volumen esférico con `math.pi`.
   - Método `es_planeta_exterior()`: Retorna un booleano determinando si el planeta se encuentra más allá de 5.2 UA.
   - Método `__str__()`: Presenta de forma legible las propiedades y clasificación astronómica.
   - Incluye instancias de prueba con salida formateada.

2. **`automovil.py`**:
   - Implementa la clase `Automovil` aplicando encapsulamiento mediante atributos privados con prefijo `_`: `_velocidad_max`, `_nivel_combustible` y `_año_fabricacion`.
   - Implementa propiedades controladas con decoradores `@property` y sus correspondientes setters con validación estricta (`ValueError` ante entradas no válidas).
   - Método `tiempo_llegada(distancia_km)`: Calcula el tiempo estimado en horas para recorrer una distancia dada.
   - Método `__str__()` descriptivo e instancias de prueba con manejo de excepciones (`try/except`).

3. **`cuentas.py`**:
   - Implementa la jerarquía bancaria aplicando herencia y encapsulamiento estricto:
     - `CuentaBancaria`: Clase base con número de cuenta, titular y saldo privado `__saldo`. Métodos validados `depositar()`, `retirar()` y `consultar_saldo()`.
     - `CuentaAhorros`: Subclase que añade `tasa_interes`, invoca `super().__init__()` y calcula el interés anual generado con `calcular_interes()`.
     - `CuentaCorriente`: Subclase que añade `limite_sobregiro`, sobrescribe `retirar()` permitiendo saldo negativo controlado y método `permite_sobregiro()`.
   - Demostración de operaciones de depósito, retiro y verificación de saldo.

4. **`README.md`**:
   - Documentación general del repositorio, detalles del estudiante y especificación de cada archivo.
