def return_nth_smallest_ascii(s):
    substring = s[1:37]
    return min(substring, key=lambda char: ord(char))