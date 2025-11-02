def calcular_propina(total, porcentaje):
    try:
        total = float(total)
        porcentaje = float(porcentaje)
    except ValueError:
        raise ValueError("Total y porcentaje deben poder convertirse a número.")
    return round(total * (porcentaje / 100.0), 2)


def main():
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
