def return_nth_smallest_ascii(s):
    char_list = list(s[50:76])
    sorted_chars = sorted(char_list, key=lambda x: ord(x))
    seventh_smallest = sorted_chars[6]
    return seventh_smallest