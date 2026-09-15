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

sure = input("Create a Folder for each file type? (y/n)")

if sure == "y":

    for i in p.iterdir():

        if i.is_file():
            fileType = i.suffix
            category = cat.get(fileType, "Desconhecido")
            print(category, '->', i.name)   

            folder = p / category
            folder.mkdir(exist_ok=True)

            shutil.move(i, folder)

        else:
            print("Pasta ->" ,"/"+ i.name)


