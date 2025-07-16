import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    #  Check if the file_path does not exist
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python3", abs_path, *args], capture_output=True, timeout=30, cwd=working_directory, text=True)
    except Exception as e:
        return f"Error: executing Python file: {e}"

    output = []
    
    if result.stdout:
        output.append(f"STDOUT: {result.stdout}")

    if result.stderr:
        output.append(f"STDERR: {result.stderr}")

    if result.returncode != 0:
        output.append(f"Process exited with code {result.returncode}")

    if len(output) > 0:
        return "\n".join(output)
    else:
        return "No output produced."


    