import re
import colorama

colorama.init(autoreset=True)

# CONSTANTS
ITERABLE_BRACES = {
    list: ["[", "]"],
    set: ["{", "}"],
    tuple: ["(", ")"],
    dict: ["{", "}"],
}


class Color:
    BLACK = colorama.Fore.BLACK
    BLUE = colorama.Fore.BLUE
    CYAN = colorama.Fore.CYAN
    GREEN = colorama.Fore.GREEN
    MAGENTA = colorama.Fore.MAGENTA
    RED = colorama.Fore.RED
    RESET = colorama.Fore.RESET
    WHITE = colorama.Fore.WHITE
    YELLOW = colorama.Fore.YELLOW


class Regex:
    FUNCTION = re.compile(r"")
    DICT = re.compile(r"")
    INTEGER = re.compile(r"")


def format_string(obj: str) -> str:
    return f'{Color.GREEN}"{obj}"'


def format_number(obj: int | float) -> str:
    return f"{Color.CYAN}{obj}"


def format_boolean(obj: bool) -> str:
    return f"{Color.MAGENTA}{obj}"


def format_iterable(obj: list | tuple | set) -> str:
    obj_type = type(obj)

    braces = ITERABLE_BRACES[obj_type]
    formatted_iterable = f"{Color.YELLOW}{braces[0]}"

    for item in obj:
        formatted_iterable += f"\n   {format(item)}{Color.RED},"

    formatted_iterable += f"\n{Color.YELLOW}{braces[1]}"

    return formatted_iterable


def format_dict(obj: dict) -> str:
    formatted_dict = f"{Color.YELLOW}{ITERABLE_BRACES[dict][0]}"

    for key, value in obj.items():
        formatted_dict += f"\n   {format(key)}{Color.RED}: {format(value)}{Color.RED},"

    formatted_dict += f"\n{Color.YELLOW}{ITERABLE_BRACES[dict][1]}"

    return formatted_dict


def format_type(obj: type) -> str:
    obj = repr(obj).split()
    return f"<{Color.RED}{obj[0][1:]} {Color.YELLOW}{obj[1][:-1]}{Color.RESET}>"


def format_object(obj) -> str:
    raise NotImplementedError("Coming Soon")


def format(obj) -> str:
    obj_type = type(obj)

    if obj_type == str:
        return format_string(obj)

    if obj_type == bool:
        return format_boolean(obj)

    if obj is None:
        return f"{Color.MAGENTA}None"

    if obj_type in {int, float}:
        return format_number(obj)

    if obj_type in {tuple, list, set}:
        return format_iterable(obj)

    if obj_type == dict:
        return format_dict(obj)

    if obj_type == type:
        # if it's a class type, not object
        # class Main: pass
        # type(Main) == type  returns >> True
        return format_type(obj)

    # else
    return format_object(obj)


def cprint(obj) -> None:
    print(format(obj))


def test():
    cprint(2)
    cprint(2.2)
    cprint("2.2")
    cprint(True)
    cprint(None)
    cprint([1, 2, "3"])
    # cprint([1, 2, "3", ["hello", 1, {"hi": 5, "25": ["Hello"]}]])
    cprint([1, 2, "3", ["hello"]])
    cprint({1: "", "2": 5, "3": "Hello"})
    cprint(Color)
    # cprint(print)

    print("\n------------------------------------------ TODO ----------------------------------\n")

    # TODO
    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age

        def __repr__(self) -> str:
            return f"Person(name={self.name}, age={self.age})"

    print(f"Input: {Person('Bob', 24)}")
    print(
        "Output: "
        f'Person({Color.RED}name{Color.RESET}={Color.GREEN}"Bob"{Color.RESET}, '
        f'{Color.RED}age{Color.RESET}={Color.CYAN}24{Color.RESET})', "\n\n"
    )

    # print(f"Input: {Person}")
    # print(f"Output: <{Color.RED}class {Color.YELLOW}'__main__.test.<locals>.Person'{Color.RESET}>\n\n")

    print("Input: <__main__.Main object at 0x000001EA2EC5F790>")
    print(
        "Output: "
        f"<{Color.YELLOW}__main__.Main{Color.RESET} object at {Color.RED}0x000001EA2EC5F790{Color.RESET}>"
    )


if __name__ == "__main__":
    test()
