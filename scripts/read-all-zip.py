import urllib.request
import zipfile
import io
import os

url = "https://v0chat-agent-data-prod.s3.us-east-1.amazonaws.com/vm-binary/GDHWLpQAzhB/258929d00ae51be8948b08244ff8b3e29f01da92e04c9f817c7dafba0edd3e9e.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA52KF4VHQDTZ5RDMT%2F20260308%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260308T011123Z&X-Amz-Expires=3600&X-Amz-Signature=48cd99e6aedfd3cf35ab341fcb12bea1690ae11b0b3c394aa0877c86224c03b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject"

print("Baixando arquivo ZIP...")
response = urllib.request.urlopen(url)
zip_data = response.read()
print(f"\nDownload concluído: {len(zip_data)} bytes")

with zipfile.ZipFile(io.BytesIO(zip_data)) as zf:
    # List all files
    print("\n=== LISTA DE ARQUIVOS ===")
    for name in sorted(zf.namelist()):
        print(name)
    
    # Read components
    components_to_read = [
        "components/header.tsx",
        "components/hero.tsx", 
        "components/how-it-works.tsx",
        "components/benefits.tsx",
        "components/social-proof.tsx",
        "components/simulation-form.tsx",
        "components/differentials.tsx",
        "components/final-cta.tsx",
        "components/footer.tsx",
        "components/scroll-progress.tsx",
        "lib/utils.ts",
        "components/ui/button.tsx",
    ]
    
    for comp in components_to_read:
        try:
            content = zf.read(comp).decode('utf-8')
            print(f"\n=== {comp} ===")
            print(content)
        except KeyError:
            print(f"\n=== {comp} === NOT FOUND")
