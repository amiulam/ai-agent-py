import os
import subprocess

from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a Python file located inside the working directory. Provide only the required parameter 'file_path' (relative path) and an optional 'args' list of strings. The working directory is injected automatically and should not be provided by the caller.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory (for example: \"main.py\" or \"pkg/module.py\")",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of command-line arguments to pass to the Python script (each item is a string)",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]

        if type(args) is list:
            command.extend([args])

        result = subprocess.run(
            command, text=True, cwd=working_dir_abs, timeout=30, capture_output=True
        )

        output_messages = []

        if result.returncode != 0:
            output_messages.append(f"Process exited with code {result.returncode}")

        if not result.stdout and not result.stderr:
            output_messages.append("No output produced")
        else:
            if result.stdout:
                output_messages.append(f"STDOUT:\n{result.stdout}")
            if result.stderr:
                output_messages.append(f"STDERR:\n{result.stderr}")

        final_output = "\n".join(output_messages)

        return final_output

    except Exception as e:
        return f"Error: executing Python file: {e}"
