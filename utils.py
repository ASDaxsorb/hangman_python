import os


def clear_terminal():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"

    os.system(command)
