class CuentaBancaria:
    """Clase base que representa una cuenta bancaria con operaciones básicas."""

    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0) -> None:
        self.numero_cuenta: str = numero_cuenta
        self.titular: str = titular
        self._saldo: float = saldo_inicial

    def depositar(self, monto: float) -> None:
        """Suma un monto al saldo tras validar que sea positivo."""
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0.")
        self._saldo += monto

    def retirar(self, monto: float) -> None:
        """Resta un monto del saldo tras validar fondos suficientes."""
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self._saldo -= monto

    def consultar_saldo(self) -> float:
        """Retorna el saldo actual de la cuenta."""
        return self._saldo

    def __str__(self) -> str:
        """Retorna la representación en cadena de la cuenta."""
        return f"Cuenta: {self.numero_cuenta} | Titular: {self.titular} | Saldo: S/. {self._saldo:.2f}"

class CuentaAhorros(CuentaBancaria):
    """Clase que representa una cuenta de ahorros con tasa de interés."""

    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0, tasa_interes: float = 0.0) -> None:
        super().__init__(numero_cuenta, titular, saldo_inicial)
        self.tasa_interes: float = tasa_interes

    def calcular_interes(self) -> float:
        """Retorna el interés anual estimado según el saldo actual."""
        return self._saldo * (self.tasa_interes / 100)

    def __str__(self) -> str:
        interes_estimado = self.calcular_interes()
        return (
            f"{super().__str__()} | Tasa Interés: {self.tasa_interes}% | "
            f"Interés Anual Estimado: S/. {interes_estimado:.2f}"