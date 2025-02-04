def generate_random_string(length: int = 8):
    import random
    import string

    return "".join(random.choices(string.ascii_letters, k=length))
