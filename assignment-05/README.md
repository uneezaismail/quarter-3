# 🛡️ VaultLock – Secure Data Encryption System

**VaultLock** is a secure and user-friendly Streamlit-based app designed to **encrypt, store, and retrieve your sensitive data** with password protection and data encryption using `cryptography`.

---

## 🚀 Features

- 🔐 **User Registration & Login**
- 🧠 **Password Hashing (PBKDF2 + SHA256)**
- 🔒 **Data Encryption with Fernet**
- 📂 **Save Encrypted Entries with Title**
- 🔎 **Retrieve & Decrypt Data by Re-entering Passkey**
- 🚫 **Brute-force Protection (Lockout on 3 Failed Attempts)**

---

## 🧰 Built With

- [Streamlit](https://streamlit.io/) – For building the UI
- [Cryptography](https://cryptography.io/) – For strong encryption
- Python’s standard libraries:
  - `os` – File handling
  - `json` – Data storage
  - `time` – Lockout timing
  - `hashlib`, `base64` – Password hashing

---

## 📁 App Sections

- **Home**: Overview and introduction
- **Account**: Register or login securely
- **Store Data**: Encrypt and save confidential info under a custom title
- **Retrieve Data**: Decrypt and access stored entries by re-entering passkey
- **Logout**: Securely end your session

---

## 🔐 Security Notes

- Passwords are **never stored in plain text**
- All user data is **encrypted with a unique Fernet key**
- Includes **lockout mechanism** to prevent brute-force login attempts
- Encryption key is stored locally – keep it safe!

---

## 💡 Use Cases

- Store private notes or credentials securely
- Keep journal entries encrypted
- Save sensitive data for personal use
- Simple vault for offline, local protection

---

## 📜 License

MIT License © 2025

---

> This is a personal project built for learning purposes. Use with care for any real sensitive data.
