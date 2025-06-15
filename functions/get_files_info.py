from os.path import abspath, getsize, isdir, isfile, join
from os import listdir


def get_files_info(working_directory: str, directory: str | None = None):
    if directory is None:
        return f"Error: current directory is None"
    working_dir = abspath(working_directory)
    cur_dir = abspath(join(working_directory, directory))
    # print(f"{working_dir=}")
    # print(f"{cur_dir=}")
    if not isdir(cur_dir):
        # print(f"Error: {cur_dir} is not a directory")
        return f"Error: {cur_dir} is not a directory"
    if not cur_dir.startswith(working_dir):
        return f"Error: Cannot list `{cur_dir}` as it is outside the permitted working directory"
    try:
        dir_string = ""
        dir_contents = listdir(cur_dir)
        for content in dir_contents:
            full_cpath = join(cur_dir, content)
            # print(f"{full_cpath=}")
            is_dir = isdir(full_cpath)
            is_file = isfile(full_cpath)
            if not is_dir and not is_file:
                return f"Error: The content '{full_cpath}' is neither a file nor a directory"
            get_size = getsize(full_cpath)
            dir_string += frame_string(content, get_size, is_dir) + "\n"
        dir_string = dir_string[:-1]
        # print(f"{dir_string=}")
        return dir_string
    except Exception as ex:
        return f"Error: {ex}"




def frame_string(name: str, size: int, is_dir: bool):
    # print(f"- {name}: file_size={size} bytes, isdir={is_dir}")
    return f"- {name}: file_size={size} bytes, is_dir={is_dir}"
