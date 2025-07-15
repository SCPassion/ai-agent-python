import os

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    dir_name = os.path.dirname(full_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    try:
        with open(full_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{full_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'