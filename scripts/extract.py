import zipfile
import os
import glob

# Encontrar o arquivo ZIP
zip_files = glob.glob("/vercel/share/v0-project/*.zip")
print(f"Arquivos ZIP encontrados: {zip_files}")

if not zip_files:
    print("Nenhum arquivo ZIP encontrado!")
else:
    zip_path = zip_files[0]
    print(f"Usando: {zip_path}")
    
    extract_path = "/vercel/share/v0-project/extracted"
    os.makedirs(extract_path, exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
        print("Arquivos extraídos:")
        for name in zip_ref.namelist():
            print(f"  - {name}")
    
    print(f"\nExtração concluída em: {extract_path}")
