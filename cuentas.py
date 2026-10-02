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

class CuentaCorriente(CuentaBancaria):
    """Clase que representa una cuenta corriente con soporte para sobregiro."""

    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0, limite_sobregiro: float = 0.0) -> None:
        super().__init__(numero_cuenta, titular, saldo_inicial)
        self.limite_sobregiro: float = limite_sobregiro

    def retirar(self, monto: float) -> None:
        """Sobrescribe retirar permitiendo quedar en negativo hasta el límite de sobregiro."""
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")
        if monto > (self._saldo + self.limite_sobregiro):
            raise ValueError("El retiro excede el límite de sobregiro permitido.")
        self._saldo -= monto

    def permite_sobregiro(self) -> bool:
        """Indica si la cuenta se encuentra actualmente en estado de sobregiro."""
        return self._saldo < 0

    def __str__(self) -> str:
        estado_sobregiro = "Sí" if self.permite_sobregiro() else "No"
        return (
            f"{super().__str__()} | Límite Sobregiro: S/. {self.limite_sobregiro:.2f} | "
            f"En sobregiro: {estado_sobregiro}"
        )


if __name__ == "__main__":
    print("--- Demostración Cuenta de Ahorros ---")
    ahorros = CuentaAhorros("AH-101", "Juan Pérez", saldo_inicial=1000.0, tasa_interes=4.5)
    ahorros.depositar(500.0)
    print(ahorros)

    print("\n--- Demostración Cuenta Corriente ---")
    corriente = CuentaCorriente("CC-202", "María López", saldo_inicial=200.0, limite_sobregiro=500.0)
    corriente.retirar(400.0)  # Queda en -200 (sobregiro dentro del límite)
    print(corriente)
