class CuentaBancaria:
    """Clase base que representa una cuenta bancaria con operaciones básicas."""

    def __init__(self, numero_cuenta: str, titular: str) -> None:
        self.numero_cuenta: str = numero_cuenta
        self.titular: str = titular
        self.__saldo: float = 0.0

    def depositar(self, monto: float) -> None:
        """Suma un monto al saldo tras validar que sea estrictamente positivo."""
        # Hotfix: validación de monto positivo en depositar
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0.")
        self.__saldo += float(monto)

    def retirar(self, monto: float) -> None:
        """Resta un monto del saldo tras validar fondos suficientes."""
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self.__saldo -= float(monto)

    def consultar_saldo(self) -> float:
        """Retorna el saldo actual de la cuenta."""
        return self.__saldo

    def __str__(self) -> str:
        """Retorna la representación legible de la cuenta."""
        return f"Cuenta: {self.numero_cuenta} | Titular: {self.titular} | Saldo: S/. {self.__saldo:.2f}"


class CuentaAhorros(CuentaBancaria):
    """Clase que representa una cuenta de ahorros con tasa de interés anual."""

    def __init__(self, numero_cuenta: str, titular: str, tasa_interes: float) -> None:
        super().__init__(numero_cuenta, titular)
        self.tasa_interes: float = float(tasa_interes)

    def calcular_interes(self) -> float:
        """Calcula y retorna el interés anual generado según el saldo actual."""
        return self.consultar_saldo() * (self.tasa_interes / 100.0)

    def __str__(self) -> str:
        interes_estimado = self.calcular_interes()
        return (
            f"{super().__str__()} | Tasa Interés: {self.tasa_interes}% | "
            f"Interés Anual Estimado: S/. {interes_estimado:.2f}"
        )


class CuentaCorriente(CuentaBancaria):
    """Clase que representa una cuenta corriente con límite de sobregiro."""

    def __init__(self, numero_cuenta: str, titular: str, limite_sobregiro: float) -> None:
        super().__init__(numero_cuenta, titular)
        self.limite_sobregiro: float = float(limite_sobregiro)

    def retirar(self, monto: float) -> None:
        """Sobrescribe retirar permitiendo quedar en negativo hasta el límite de sobregiro."""
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")
        if monto > (self.consultar_saldo() + self.limite_sobregiro):
            raise ValueError("El retiro excede el límite de sobregiro permitido.")
        self._CuentaBancaria__saldo -= float(monto)

    def permite_sobregiro(self) -> bool:
        """Indica si la cuenta se encuentra actualmente en sobregiro (saldo negativo)."""
        return self.consultar_saldo() < 0

    def __str__(self) -> str:
        estado_sobregiro = "Sí" if self.permite_sobregiro() else "No"
        return (
            f"{super().__str__()} | Límite Sobregiro: S/. {self.limite_sobregiro:.2f} | "
            f"En sobregiro: {estado_sobregiro}"
        )


if __name__ == "__main__":
    print("--- Demostración Cuenta de Ahorros ---")
    ahorros = CuentaAhorros("AH-101", "Juan Pérez", tasa_interes=4.5)
    ahorros.depositar(1000.0)
    print(ahorros)
    print(f"Interés calculado: S/. {ahorros.calcular_interes():.2f}")

    print("\n--- Demostración Cuenta Corriente ---")
    corriente = CuentaCorriente("CC-202", "María López", limite_sobregiro=200.0)
    corriente.depositar(100.0)
    print(corriente)
    corriente.retirar(250.0)  # Saldo: -150.0
    print(corriente)
    print(f"¿En sobregiro?: {corriente.permite_sobregiro()}")
