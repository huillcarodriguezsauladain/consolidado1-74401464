import math


class Planeta:
    """Clase que representa un planeta del sistema solar."""

    def __init__(
        self,
        nombre: str,
        masa: float,
        radio: float,
        distancia_al_sol: float,
        tiene_vida: bool = False
    ) -> None:
        self.nombre: str = nombre
        self.masa: float = float(masa)
        self.radio: float = float(radio)
        self.distancia_al_sol: float = float(distancia_al_sol)
        self.tiene_vida: bool = bool(tiene_vida)

    def calcular_densidad(self) -> float:
        """Calcula y retorna la densidad media del planeta en kg/m³."""
        volumen: float = (4 / 3) * math.pi * (self.radio ** 3)
        return self.masa / volumen

    def es_planeta_exterior(self) -> bool:
        """Determina si es un planeta exterior (distancia al Sol > 5.2 UA)."""
        return self.distancia_al_sol > 5.2

    def __str__(self) -> str:
        """Retorna una cadena con el nombre, densidad calculada y si es exterior o interior."""
        tipo: str = "exterior" if self.es_planeta_exterior() else "interior"
        densidad: float = self.calcular_densidad()
        vida: str = "Sí" if self.tiene_vida else "No"
        return (
            f"Planeta: {self.nombre} | "
            f"Densidad: {densidad:.2f} kg/m³ | "
            f"Clasificación: planeta {tipo} | "
            f"Tiene vida: {vida}"
        )


if __name__ == "__main__":
    tierra = Planeta(
        nombre="Tierra",
        masa=5.972e24,
        radio=6371000.0,
        distancia_al_sol=1.0,
        tiene_vida=True
    )

    jupiter = Planeta(
        nombre="Júpiter",
        masa=1.898e27,
        radio=69911000.0,
        distancia_al_sol=5.204,
        tiene_vida=False
    )

    print(tierra)
    print(jupiter)