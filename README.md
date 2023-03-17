# PDFEncryption
Encrypt and decrypt multiple PDF files using AES. Purposes online sharing. The malicious thrid party (eg. cloud storage, chat app, etc.) cannot access the PDF without key file.
## A. Download
[Windows](https://github.com/HaozheTian/PDFEncryption/raw/main/dist/pdf_coder.exe)
## B. Usage
### B.1 Generate key file

``cd`` to the directory where ``utils.py`` is stored.
Use console command to generate key file:
```console
python utils.py -p 'key.key'
```
 The string after ``-p`` or ``--path`` is the name of the key file (must end in `.key`, defaults to `'key.key'`). Keep the key file safe as the file will be used for encryption and decryption. **do not upload online**.

 **Warning:** If the key file is lost, the encrypted file cannot be recovered. It is your responsiblity to keep the key file safe.

### B.2 Encryption and decryption:
Select key file, then select in explorer for encryption or decryption.