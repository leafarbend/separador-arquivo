import os
from tkinter.filedialog import askdirectory 

caminho = askdirectory(title= "Selecione uma pasta")
arquivos_lista = os.listdir(caminho) 

locais = {
    "imagens" : [".png", ".jpg"],
    "pdfs" : [".pdf"],
    "docs" : [".doc", ".docx"],
    
}


for arquivo in arquivos_lista:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
