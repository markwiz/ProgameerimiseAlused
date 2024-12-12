def func():
    """Print to console"""
    print("Im inside the function")


def my_name_is(name:str) -> None:
    """Print to console - My name is [name]"""
    print(f"My name is {name}")


def sum_six(num:int):
    return num + 6


def sum_numbers(num1, num2):
    return num1 + num2


def usd_to_eur(usd:int):
    return usd * 0.8

print(usd_to_eur(1000))








if __name__ == "__main__":
    func()
    my_name_is("My name is Mark")
    my_name_is("My name is Kuusik")
