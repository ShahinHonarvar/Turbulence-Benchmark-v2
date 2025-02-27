def return_n_smallest_chars(string):
    chars = []
    for char in string:
        if len(chars) < 49 or ord(char) < ord(chars[-1]):
            chars.append(char)
    chars.sort(key=lambda x: -ord(x))
    return chars