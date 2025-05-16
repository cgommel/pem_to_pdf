import os
from pathlib import Path
import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from io import BytesIO
from PIL import Image
from reportlab.lib.utils import ImageReader


def create_qr_pdf(input_dir: str, output_dir: str):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for pem_file in input_path.glob("*.pem"):
        with open(pem_file, "r", encoding="utf-8") as f:
            content = f.read()

        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(content)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black",
                            back_color="white").convert("RGB")

        img_buffer = BytesIO()
        img.save(img_buffer, format="PNG")
        img_buffer.seek(0)
        img_reader = ImageReader(img_buffer)

        pdf_filename = output_path / f"{pem_file.stem}.pdf"
        c = canvas.Canvas(str(pdf_filename), pagesize=A4)
        width, height = A4

        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width / 2, height - 2 * cm, pem_file.name)

        img_size_cm = 15
        img_size = img_size_cm * cm
        x = (width - img_size) / 2
        y = (height - img_size) / 2 - 2 * cm

        c.drawImage(img_reader, x, y, width=img_size, height=img_size)

        c.showPage()
        c.save()

    print(f"Fertig! PDFs gespeichert in: {output_path}")


if __name__ == "__main__":
    create_qr_pdf("pem_input", "qr_pdfs")
