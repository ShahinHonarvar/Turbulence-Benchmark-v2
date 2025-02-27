def return_nth_smallest_ascii(string):
    chars = [char for char in string[1:37]]
    chars.sort(key=lambda c: ord(c))
    return chars[14]