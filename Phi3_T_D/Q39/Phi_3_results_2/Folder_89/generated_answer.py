def return_n_greatest_chars(s):
    return sorted([char for char in set(s) if ord(char) > ord('0') - 55])