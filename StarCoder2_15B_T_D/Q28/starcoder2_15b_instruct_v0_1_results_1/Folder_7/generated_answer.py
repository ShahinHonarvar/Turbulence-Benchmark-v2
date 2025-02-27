def return_nth_smallest_ascii(string):
    chars = [char for char in string[12:56]]
    chars.sort(key=lambda c: ord(c))
    return chars[16]