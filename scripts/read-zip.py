import urllib.request
import zipfile
import io
import base64
import json

# URL do arquivo ZIP
url = "https://v0chat-agent-data-prod.s3.us-east-1.amazonaws.com/vm-binary/GDHWLpQAzhB/258929d00ae51be8948b08244ff8b3e29f01da92e04c9f817c7dafba0edd3e9e.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA52KF4VHQDTZ5RDMT%2F20260308%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260308T011123Z&X-Amz-Expires=3600&X-Amz-Signature=48cd99e6aedfd3cf35ab341fcb12bea1690ae11b0b3c394aa0877c86224c03b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject"

print("Baixando arquivo ZIP...")
response = urllib.request.urlopen(url)
zip_data = response.read()
print(f"Download concluído: {len(zip_data)} bytes\n")

# Ler package.json do ZIP
with zipfile.ZipFile(io.BytesIO(zip_data)) as zf:
    # Mostrar package.json
    print("=== package.json ===")
    print(zf.read("package.json").decode('utf-8'))
    print("\n")
    
    # Mostrar layout.tsx
    print("=== app/layout.tsx ===")
    print(zf.read("app/layout.tsx").decode('utf-8'))
    print("\n")
    
    # Mostrar page.tsx
    print("=== app/page.tsx ===")
    print(zf.read("app/page.tsx").decode('utf-8'))
    print("\n")
    
    # Mostrar globals.css
    print("=== app/globals.css ===")
    print(zf.read("app/globals.css").decode('utf-8'))
