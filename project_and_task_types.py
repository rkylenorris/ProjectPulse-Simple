from enum import Enum

DEFAULT_PROJECT_TYPES = ["PERSONAL", "PROFESSIONAL"]
PROJECT_TYPES_PATH = "pulse/config/Project_Types.txt"
DEFAULT_TASK_TYPES = ["ADD", "REMOVE", "REFACTOR", "TEST"]
TASK_TYPES_PATH = "pulse/config/Task_types.txt"


def enum_from_config(config_path: str, kinds: list, proj: bool):
    with open(config_path, 'r') as f:
        lines = [line.upper().strip(" \n") for line in f.readlines() if line[0].isalpha()]
        lines_exist = [line for line in lines if line in kinds]
        if len(lines) > 0:
            if len(lines_exist) == 0:
                for line in lines:
                    kinds.append(line)
            elif len(lines_exist) >=1:
                print(f"WARNING: you added a project type that is already a default {lines_exist}")
                for line in linew:
                    if line not in lines_exist:
                        kinds.append(line)
    if proj:
        enum_name = "ProjectType"
    else:
        enum_name = "TaskType"

    return Enum(enum_name, {s: i for i, s in enumerate(kinds)})


ProjectTypes = enum_from_config(PROJECT_TYPES_PATH, DEFAULT_PROJECT_TYPES, True)
TaskTypes = enum_from_config(TASK_TYPES_PATH, DEFAULT_TASK_TYPES, False)