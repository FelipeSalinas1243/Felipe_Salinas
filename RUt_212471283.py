# Función para realizar las comparaciones para el Switch 1
def comparar_switch1(native_vlan_switch1, vlan_switch1):
    # Comparación de la VLAN nativa
    if native_vlan_switch1 == 99 and set(vlan_switch1) == {10, 20, 30}:
        print("Para el Switch 1:")
        print("Las VLANs son iguales y cumplen con el requerimiento")
    else:
        print("Para el Switch 1:")
        print("Las VLANs son diferentes y no cumplen con el requerimiento")

# Función para realizar las comparaciones para el Switch 2
def comparar_switch2(native_vlan_switch2, vlan_switch2):
    # Comparación de la VLAN nativa
    if native_vlan_switch2 == 200 and set(vlan_switch2) == {40, 50, 60}:
        print("Para el Switch 2:")
        print("Las VLANs son iguales y cumplen con el requerimiento")
    else:
        print("Para el Switch 2:")
        print("Las VLANs son diferentes y no cumplen con el requerimiento")

# Solicitar al usuario la VLAN nativa del Switch 1 y sus VLANs creadas
native_vlan_switch1 = int(input("Introduce la VLAN nativa del Switch 1: "))
vlan_switch1 = list(map(int, input("Introduce las VLANs creadas del Switch 1 separadas por espacio: ").split()))

# Solicitar al usuario la VLAN nativa del Switch 2 y sus VLANs creadas
native_vlan_switch2 = int(input("Introduce la VLAN nativa del Switch 2: "))
vlan_switch2 = list(map(int, input("Introduce las VLANs creadas del Switch 2 separadas por espacio: ").split()))

# Realizar las comparaciones para el Switch 1
comparar_switch1(native_vlan_switch1, vlan_switch1)

# Realizar las comparaciones para el Switch 2
comparar_switch2(native_vlan_switch2, vlan_switch2)

