from OpenSSL import crypto


def generate_self_signed_cert(cert_file, key_file, common_name):
    # Crear una clave privada
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 4096)  # RSA 4096 bits

    # Crear un certificado autofirmado
    cert = crypto.X509()
    cert.get_subject().CN = common_name
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(31536000)  # Validez de 1 año
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha256')

    # Guardar la clave privada y el certificado en archivos
    with open(cert_file, "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    with open(key_file, "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

    print(f"Certificado guardado como {cert_file}")
    print(f"Clave privada guardada como {key_file}")


def main_menu():
    while True:
        print("\nMenu:")
        print("1. Crear certificado")
        print("2. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            base_name = input("Ingrese el nombre base para el certificado y la clave privada (sin extensión): ")
            common_name = input("Ingrese el nombre común para el certificado (e.g., '*.barcelona2009.net'): ")
            cert_name = f"{base_name}.cer"
            key_name = f"{base_name}.key"
            generate_self_signed_cert(cert_name, key_name, common_name)
        elif choice == "2":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main_menu()