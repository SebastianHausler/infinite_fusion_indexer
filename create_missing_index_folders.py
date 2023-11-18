# Author: DamonDragon
import os
from pathlib import Path
from typing import List

# Static variables
GRAPHICS_FOLDER = "Graphics"
CUSTOM_BATTLERS_FOLDER = "CustomBattlers"
INDEXED_FOLDER = "indexed"


def main():
    sprite_path = get_sprite_path()
    file_list = get_png_file_list(sprite_path)
    print(file_list)
    create_folders(file_list, sprite_path)


def get_png_file_list(path_to_read) -> List[str]:
    file_list: List[str] = os.listdir(path_to_read)
    file_list = get_png_list_from_folder(file_list)
    file_list = split_list(file_list)
    return list(set(file_list))


def create_folders(file_list: List[str], sprite_path):
    for sprite in file_list[:]:
        Path(sprite_path / INDEXED_FOLDER / sprite).mkdir(parents=True, exist_ok=True)


def get_png_list_from_folder(file_list: List[str]):
    # file_list[:] makes a copy of file_list.
    for sprite in file_list[:]:
        if not sprite.endswith(".png"):
            file_list.remove(sprite)
    return file_list


def split_list(file_list: List[str]):
    return [item.split('.')[0] for item in file_list]


def get_sprite_path():
    current_path = Path.cwd()

    if check_for_str_in_folder(GRAPHICS_FOLDER):
        return current_path / GRAPHICS_FOLDER / CUSTOM_BATTLERS_FOLDER

    elif check_for_str_in_folder(CUSTOM_BATTLERS_FOLDER) and current_path.name == GRAPHICS_FOLDER:
        return current_path / CUSTOM_BATTLERS_FOLDER

    elif current_path.name == CUSTOM_BATTLERS_FOLDER or check_for_str_in_folder(INDEXED_FOLDER):
        return current_path

    else:
        return current_path


def check_for_str_in_folder(folder: str):
    # Checks if a folder exists in the current directory
    return folder in os.listdir()


if __name__ == '__main__':
    main()
