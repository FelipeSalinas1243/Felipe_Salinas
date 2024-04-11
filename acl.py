# Función para identificar el tipo de ACL IPv4
def identificar_tipo_acl(numero_acl):
    if 0 <= numero_acl <= 99:
        return "ACL Estándar"
    elif 100 <= numero_acl <= 199:
        return "ACL Extendida"
    else:
        return "El número no corresponde a una lista de acceso"

# Solicitar al usuario el número de ACL IPv4
numero_acl = int(input("Introduce el número de ACL IPv4: "))

# Imprimir el tipo de ACL IPv4
print("Tipo de ACL IPv4:", identificar_tipo_acl(numero_acl))
