import zipfile
import os

zip_path = "/vercel/share/v0-project/b_JDrUkv8a0eC-1772631931078.zip"
extract_path = "/vercel/share/v0-project/extracted"

os.makedirs(extract_path, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
    print("Arquivos extraídos:")
    for name in zip_ref.namelist():
        print(f"  - {name}")

print(f"\nExtração concluída em: {extract_path}")
