class Automovil:
    """Clase que representa un automóvil con validaciones mediante @property."""

    def __init__(
        self,
        marca: str,
        modelo: str,
        velocidad_max: float,
        nivel_combustible: float,
        año_fabricacion: int
    ) -> None:
        self.marca: str = marca
        self.modelo: str = modelo
        # Atributos privados inicializados mediante setters
        self.velocidad_max = velocidad_max
        self.nivel_combustible = nivel_combustible
        self.año_fabricacion = año_fabricacion

    @property
    def velocidad_max(self) -> float:
        """Getter para la velocidad máxima en km/h."""
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor: float) -> None:
        """Setter con validación: debe ser estrictamente mayor a 0."""
        if valor <= 0:
            raise ValueError("La velocidad máxima debe ser mayor a 0 km/h.")
        self._velocidad_max = valor

    @property
    def nivel_combustible(self) -> float:
        """Getter para el nivel de combustible (porcentaje 0.0 a 100.0)."""
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor: float) -> None:
        """Setter con validación: debe estar entre 0.0 y 100.0."""
        if not (0.0 <= valor <= 100.0):
            raise ValueError("El nivel de combustible debe estar entre 0.0 y 100.0%.")
        self._nivel_combustible = valor

    @property
    def año_fabricacion(self) -> int:
        """Getter para el año de fabricación."""
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor: int) -> None:
        """Setter con validación: debe estar entre 1886 y 2026."""
        if not (1886 <= valor <= 2026):
            raise ValueError("El año de fabricación debe estar entre 1886 y 2026.")
        self._año_fabricacion = valor
    def tiempo_llegada(self, distancia_km: float) -> float:
        """Calcula el tiempo estimado de llegada en horas."""
        return distancia_km / self.velocidad_max

    def __str__(self) -> str:
        """Retorna la representación legible del automóvil."""
        return (
            f"Automóvil: {self.marca} {self.modelo} ({self.año_fabricacion}) | "
            f"Vel. Máx: {self.velocidad_max} km/h | "
            f"Combustible: {self.nivel_combustible}%"
        )


if __name__ == "__main__":
    auto1 = Automovil(
        marca="Toyota",
        modelo="Corolla",
        velocidad_max=180.0,
        nivel_combustible=75.5,
        año_fabricacion=2022
    )

    print(auto1)
    distancia = 360.0
    print(f"Tiempo para recorrer {distancia} km: {auto1.tiempo_llegada(distancia):.2f} horas")

    # Demostración de prueba de validación con try/except
    print("\n--- Probando validación de año incorrecto ---")
    try:
        auto1.año_fabricacion = 1800  # Lanza ValueError
    except ValueError as e:
        print(f"Error capturado exitosamente: {e}")