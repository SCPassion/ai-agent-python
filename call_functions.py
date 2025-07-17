from google.genai import types
from functions.get_files_info import *
from functions.run_python_file import *
from functions.write_file import *
from functions.get_file_content import *

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_run_python_file,
        schema_write_file,
        schema_get_file_content,
    ]
)

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args

    function_args["working_directory"] = "./calculator"
    
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")
    
    if function_name == "get_files_info":
        function_result = get_files_info(**function_args)
    elif function_name == "run_python_file":
        function_result = run_python_file(**function_args)
    elif function_name == "write_file":
        function_result = write_file(**function_args)
    elif function_name == "get_file_content":
        function_result = get_file_content(**function_args)
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
        