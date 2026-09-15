from pathlib import Path
import shutil

p = Path('./manager-files/files')
print("==========================================================")
print("Pasta atual: ", p)

cat = {
    '.png' : 'Imagem',
    '.jpg' : 'Imagem',
    '.jpeg' : 'Imagem',
    '.webp' : 'Imagem',
    '.txt' : 'Texto',
    '.md' : 'Texto',
    '.pdf' : 'Documento',
    '.docx' : 'Documento',
    '.xlsx' : 'Documento',
    '.pptx' : 'Documento',
    '.mp3' : 'Audio',
    '.mp4' : 'Video',
    '.mkv' : 'Video',
    '.zip' : 'Compactado',
    '.tar' : 'Compactado'
}

for i in p.iterdir():

    if i.is_file():
        fileType = i.suffix
        print(cat.get(fileType, "Desconhecido"), '->', i.name)   

    else:
        print("Pasta ->" ,"/"+i.name)

    sure = input("Create a Folder for each file type? (y/n)")
    
    if sure == "y":
        print(1)


