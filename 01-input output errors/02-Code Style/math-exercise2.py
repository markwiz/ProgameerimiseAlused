def ask_name_and_greet_user(THABsss):
    """
    Ask name and greet user.

    The user has to enter his/her name. The function prints the greeting.

    Regular greeting: Hi, [name]. Would you like to have a Hamburger?
    [name] is capitalized, meaning first letter is capital, the rest is lower.

    If the name is Thanos (case insensitive, so thanos and THANOS also count):
    Get out of here, Thanos! Nobody wants to play with you!
    """
    # code here
    name = input("What is your name?: ")
    capitalized_named = name.capitalize()
    if capitalized_named:
        print(f"Hi, {capitalized_named}. Would you like to have a hamburger?")
    else:
        print("Get out of here, Thanos! Nobody wants to play with you!")

