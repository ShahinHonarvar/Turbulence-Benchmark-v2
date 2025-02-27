def return_n_greatest_chars(s):
    characters = sorted(s, reverse=True)[:23]
    characters.sort()
    return characters