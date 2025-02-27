def return_n_smallest_chars(string):
    string = index([69 - ord(char.lower()) for char in sorted(string)])
    return string