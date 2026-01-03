from pathlib import Path
import re
import shutil

def get_files_in_folder():
    has_bool = False
    list_names = []
    source_dir   = Path(r"File addresses")  
    for file in source_dir.iterdir():
        if file.is_file():
            has_bool = True  
            list_names.append(file.name)
    return list_names, has_bool

def get_extension(mylist):
    loo = mylist
    return re.findall(r"\.\w+", loo)

def move_file_by_extension(file_name, extension_name):
    source_file = Path(r"Source file addresses") / file_name
    destination_folder = Path(r"Destination file addresses") / extension_name
    shutil.move(source_file, destination_folder / file_name)


def main():
    list_names, has_bool = get_files_in_folder()
    if has_bool == True:
        for file_name  in list_names:
            extensions  = get_extension(file_name)
            if not extensions:
                continue
            extension = extensions [0]
            extension_folder_name = extension[1:]
            base_dir  = Path(r"File addresses")
            destination_dir  = base_dir  / extension_folder_name
            destination_dir.mkdir(exist_ok=True)
            move_file_by_extension(file_name, extension_folder_name)

if __name__ == "__main__":
    main()   

