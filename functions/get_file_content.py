import os

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = (
            os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        )

        if not os.path.isfile(target_file):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        if not valid_target_file:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        content = ""

        with open(target_file, "r") as f:
            content += f.read(MAX_CHARS)
            if f.read(MAX_CHARS):
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

        return content
    except Exception as e:
        return f"Error: {e}"
