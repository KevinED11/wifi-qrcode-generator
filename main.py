from wifi_qrcode_generator import wifi_qrcode


def generate_wifi_qrcode(password: str, authentication_type: str = "WPA") -> None:
    qr_code = wifi_qrcode(
        "clcoding",
        hidden=False,
        authentication_type=authentication_type,
        password=password,
    )
    qr_code_image = qr_code.make_image()
    qr_code_image.save("personal_wifi.png")


def main() -> None:
    generate_wifi_qrcode(password="XC7eA3TXc4")


if __name__ == "__main__":
    main()
