def return_n_smallest_chars(chars):
    sorted_characters = sorted(chars, key=lambda x: (ord(x), -ord(x)))
    smallest_59_chars = sorted_characters[:59]
    smallest_59_chars.sort(reverse=True)
    return smallest_59_chars