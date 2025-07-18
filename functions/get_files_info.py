import os
from google.genai import types

def get_files_info(working_directory, directory=None):

    full_path = os.path.join(working_directory, directory) if directory else working_directory

    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
        
    list_dir = os.listdir(full_path)
    output_list = []
    try:
        for dir_item in list_dir:
            is_dir = os.path.isdir(os.path.join(full_path, dir_item))
            item_path = os.path.join(full_path, dir_item)
            output_list.append(f"- {dir_item}: file_size={os.path.getsize(item_path)} bytes, is_dir={is_dir}")

        return "\n".join(output_list)
    except Exception as e:
        return f'Error: {str(e)}'

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)