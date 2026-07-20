import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://hochzeit.ute-ergotherapie.at')
qr.make(fit=True)

# image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), 
img_1 = qr.make_image(back_color=(244, 245, 236), fill_color=(102, 114, 61))
img_1.save('qr.png')