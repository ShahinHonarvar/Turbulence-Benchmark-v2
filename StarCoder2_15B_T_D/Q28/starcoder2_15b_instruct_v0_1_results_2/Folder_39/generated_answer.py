def return_nth_smallest_ascii(string):
    substring = string[1:67]
    sorted_characters = sorted(substring)
    return sorted_characters[7]