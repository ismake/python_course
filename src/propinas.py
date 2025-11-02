def calcular_propina(total, porcentaje):
    """
    Calcula el monto de la propina basado en el total y porcentaje.

    Args:
        total (str/float): Total de la cuenta
        porcentaje (str/float): Porcentaje de propina

    Returns:
        float: Monto de la propina redondeado a 2 decimales

    Raises:
        ValueError: Si los argumentos no son numéricos
    """
    try:
        total = float(total)
        porcentaje = float(porcentaje)
    except ValueError:
        raise ValueError("Total y porcentaje deben poder convertirse a número.")
    return round(total * (porcentaje / 100.0), 2)


def main():
    """Función principal que ejecuta la calculadora de propinas."""
    print("Calculadora de propinas")
    total = input("Ingresa el total de la cuenta (por ejemplo 345.50): ").strip()
    porcentaje = input("Ingresa el porcentaje de propina (por ejemplo 15): ").strip()

    try:
        propina = calcular_propina(total, porcentaje)
    except ValueError as e:
        print("Error:", e)
        return

    print(f"Total: {total} — Propina ({porcentaje}%): ${propina}")
    print(f"Total a pagar: ${round(float(total) + propina, 2)}")


if __name__ == "__main__":
    main()
