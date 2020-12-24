def dice():
    import random
    a = random.randint(1, 4)
    b = random.randint(1, 4)
    print(f"dice:{a} {b}")
    if a == b:
        print("Fantastic!! You can move three times")
        return a
    else:
        return [a, b]
