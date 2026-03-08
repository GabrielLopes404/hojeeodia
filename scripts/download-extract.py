import urllib.request
import zipfile
import os
import io

zip_url = "https://v0chat-agent-data-prod.s3.us-east-1.amazonaws.com/vm-binary/GDHWLpQAzhB/8832f1cf8709133fc71a96aeaacd46ba2c3982cffdd0b570eeae65f828d567ce.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA52KF4VHQDTZ5RDMT%2F20260308%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260308T010944Z&X-Amz-Expires=3600&X-Amz-Signature=a73372eb65bfa4656992d811695f6cf015bb1c669071a4d79e0018b8d065d7e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject"

extract_path = "/vercel/share/v0-project/extracted"

print("Baixando arquivo ZIP...")
response = urllib.request.urlopen(zip_url)
zip_data = response.read()
print(f"Download concluído: {len(zip_data)} bytes")

os.makedirs(extract_path, exist_ok=True)

print("Extraindo arquivos...")
with zipfile.ZipFile(io.BytesIO(zip_data), 'r') as zip_ref:
    zip_ref.extractall(extract_path)
    print("Arquivos extraídos:")
    for name in zip_ref.namelist():
        print(f"  - {name}")

print(f"\nExtração concluída em: {extract_path}")
