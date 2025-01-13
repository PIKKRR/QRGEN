import qrcode
from PIL import Image

# URL de tu perfil de GitHub
github_url = "https://pikkrr.github.io/Portfolio2.0"

# Generar el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(github_url)
qr.make(fit=True)

# Crear la imagen del QR
qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Cargar el logo de GitHub (asegúrate de tener un logo en PNG)
logo_path = "github_logo.png"  # Cambia por la ruta de tu logo
logo = Image.open(logo_path)

# Si el logo tiene transparencia, asegúrate de convertirlo a RGBA
logo = logo.convert("RGBA")

# Redimensionar el logo para que se ajuste al centro del QR
logo_size = (qr_image.size[0] // 4, qr_image.size[1] // 4)
logo = logo.resize(logo_size, Image.Resampling.LANCZOS)

# Posicionar el logo en el centro del QR
logo_position = (
    (qr_image.size[0] - logo.size[0]) // 2,
    (qr_image.size[1] - logo.size[1]) // 2,
)

# Crear una máscara de la transparencia del logo
logo_mask = logo.convert("L").point(lambda x: min(x, 255))

# Pegar el logo sobre el QR utilizando la máscara para la transparencia
qr_image.paste(logo, logo_position, mask=logo_mask)

# Guardar el QR personalizado
qr_image.save("github_profile_qr_with_logo.png")
print("Código QR generado y guardado como github_profile_qr_with_logo.png")

