def return_n_greatest_chars(string):
    characters = list(string)
    characters.sort(key=lambda x: ord(x), reverse=True)
    return sorted(characters[:55])