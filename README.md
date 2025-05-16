# PEM to QR PDF Converter

This Python script reads all `.pem` files from an input directory and generates a separate PDF for each file. Each PDF is formatted for DIN A4 portrait layout and contains:

- The filename of the PEM key
- A large QR code representing the full content of the PEM file

This allows for easy creation of **paper backups** of cryptographic keys.

---

## 🔐 Purpose & Security Notes

This tool is designed to **archive private keys on paper** by converting them into scannable QR codes.

Normally, private keys are encrypted with a passphrase. For long-term offline backups, however, you may **deliberately omit the passphrase** to avoid losing access due to a forgotten password years later.

⚠️ **In this case, physical security is critical**:

- Keep printed keys in a secure, offline place (e.g., safe or lockbox)
- Never leave printed keys unattended or exposed
- Do not digitize or upload printed keys to any device or cloud storage

---

## 📦 Setup

### 1. Create a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. Install dependencies

Make sure `requirements.txt` is in the project directory, then:

```bash
pip install -r requirements.txt
```

If you are installing manually, the core dependencies are:

```bash
pip install "qrcode[pil]" reportlab
```

> Note: If you're using `zsh`, remember to quote the extras: `"qrcode[pil]"`.

---

## ▶️ Usage

1. Place your unencrypted `.pem` files in the folder:

   ```
   pem_input/
   ```

2. Run the script:

   ```bash
   python script.py
   ```

3. Output PDFs will be generated in:

   ```
   qr_pdfs/
   ```

Each PDF contains one large QR code and the filename of the corresponding `.pem` file.

---

## ✅ Example: Creating a 2048-bit RSA Key for Testing

```bash
openssl genpkey -algorithm RSA -out demo.pem -pkeyopt rsa_keygen_bits:2048
```

Place this `demo.pem` in the `pem_input/` folder to test the script.

---

## 📄 License

This project is open-source and provided without warranty. Use responsibly.
