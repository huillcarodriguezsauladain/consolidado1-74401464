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