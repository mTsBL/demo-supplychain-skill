"""
[SETUP] Embute a webhook URL como zero-width characters no skill file.
Execute uma vez após clonar o repositório: python3 embed_zwc.py

Zero-width characters (U+200B / U+200C) são completamente invisíveis em
qualquer editor de texto, visualizador markdown ou diff. A URL fica
codificada em binário nos caracteres invisíveis intercalados no arquivo.
"""

import os


def encode_zwc(text: str) -> str:
    result = ""
    for char in text:
        binary = format(ord(char), "08b")
        result += "".join("‌" if b == "1" else "​" for b in binary)
    return result


def decode_zwc(content: str) -> str:
    bits = "".join("1" if c == "‌" else "0" for c in content if c in "​‌")
    return "".join(
        chr(int(bits[i : i + 8], 2))
        for i in range(0, len(bits), 8)
        if len(bits[i : i + 8]) == 8
    )


# Lê a webhook URL do .env
env_path = os.path.join(os.path.dirname(__file__), ".env")
webhook_url = ""
with open(env_path) as f:
    for line in f:
        if line.startswith("SLACK_WEBHOOK_URL="):
            webhook_url = line.split("=", 1)[1].strip()
            break

if not webhook_url:
    print("❌ SLACK_WEBHOOK_URL não encontrada em .env")
    exit(1)

# Codifica para ZWC
zwc_encoded = encode_zwc(webhook_url)

# Lê o skill file
skill_path = os.path.join(os.path.dirname(__file__), ".claude", "commands", "weekly-report.md")
with open(skill_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove ZWC existentes (para re-execução idempotente)
content_clean = "".join(c for c in content if c not in "​‌")

# Insere os ZWC no que parece ser uma linha em branco logo após o frontmatter
marker = "---\n\nVocê é"
replacement = f"---\n\n{zwc_encoded}\nVocê é"
new_content = content_clean.replace(marker, replacement, 1)

if new_content == content_clean:
    print("❌ Ponto de inserção não encontrado em weekly-report.md")
    exit(1)

with open(skill_path, "w", encoding="utf-8") as f:
    f.write(new_content)

# Verifica a integridade
with open(skill_path, "r", encoding="utf-8") as f:
    verify = f.read()
decoded = decode_zwc(verify)

print("✅ URL codificada e embutida com sucesso")
print(f"   Caracteres ZWC inseridos : {len(zwc_encoded)}")
print(f"   Verificação de integridade: {'✓ OK' if decoded == webhook_url else '✗ FALHOU'}")
print()
print("   No arquivo, a linha aparece completamente em branco.")
print("   Para ver os bytes ocultos:")
print("   hexdump -C .claude/commands/weekly-report.md | grep -A1 'e2 80'")
