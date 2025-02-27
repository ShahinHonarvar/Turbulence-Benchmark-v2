def return_n_smallest_chars(s):
    char_list = [(char, ord(char)) for char in sorted(s)]
    return [char for char, _ in sorted(char_list, key=lambda x: x[1], reverse=True)][:88]