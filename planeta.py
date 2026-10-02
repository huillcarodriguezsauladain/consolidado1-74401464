import math


class planeta:
    """Clase que representa un planeta de nuestro sistema solar"""

    def __init__(
        self,
        nombre: str,
        masa: float,
        radio: float,
        distancia_al_sol: float,
        tiene_vida: bool = False
    )->None:
        self,nombre: str = nombre
        self,masa: str = masa
        self,radio: str = radio
        self,distancia_al_sol: str = distancia_al_sol
        self,tiene_vida: str = tiene_vida

    def calcular_densidad(self) -> float:
        """Calcula y retorna la densidad media del planeta en kg/m³."""
        volumen: float = (4 / 3) * math.pi * (self.radio ** 3)
        return self.masa / volumen

    def es_planeta_exterior(self) -> bool:
        """Determina si es un planeta exterior (distancia mayor a 5.2 UA)."""
        return self.distancia_al_sol > 5.2

    def __str__(self) -> str:
        """Retorna una cadena formateada con la información general del planeta."""
        tipo_planeta: str = "Exterior" if self.es_planeta_exterior() else "Interior"
        densidad_calculada: float = self.calcular_densidad()
        presencia_vida: str = "Sí" if self.tiene_vida else "No"

        return (
            f"Planeta: {self.nombre} | "
            f"Densidad: {densidad_calculada:.2f} kg/m³ | "
            f"Tipo: {tipo_planeta} | "
            f"Tiene vida: {presencia_vida}"
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