import urllib.request
import zipfile
import io
import os
import shutil

# URL do arquivo ZIP
url = "https://v0.blob.core.windows.net/b/b_JDrUkv8a0eC.zip"

print("Baixando arquivo ZIP...")
response = urllib.request.urlopen(url)
zip_data = response.read()
print(f"Download concluído: {len(zip_data)} bytes")

# Extrair para memória e listar conteúdo
print("\nConteúdo do ZIP:")
with zipfile.ZipFile(io.BytesIO(zip_data)) as zf:
    for name in zf.namelist():
        print(f"  {name}")
    
    # Extrair cada arquivo
    for name in zf.namelist():
        if name.endswith('/'):
            continue
        
        # Ler conteúdo do arquivo
        content = zf.read(name)
        
        # Salvar no diretório atual
        output_path = f"/vercel/share/v0-project/{name}"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'wb') as f:
            f.write(content)
        print(f"Criado: {output_path}")

print("\nProjeto configurado com sucesso!")
