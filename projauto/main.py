import os
import shutil
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
arquivos_lista = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".jpeg"],
    "pdfs": [".pdf"],
    "docs": [".doc", ".docx"],
}

for arquivo in arquivos_lista:
    caminho_arquivo = os.path.join(caminho, arquivo)

    # garante que é arquivo
    if os.path.isfile(caminho_arquivo):
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        for pasta in locais:
            if extensao in locais[pasta]:
                destino_pasta = os.path.join(caminho, pasta)

                os.makedirs(destino_pasta, exist_ok=True)

                destino_arquivo = os.path.join(destino_pasta, arquivo)

                print(f"Movendo: {arquivo} -> {pasta}")

                shutil.move(caminho_arquivo, destino_arquivo)