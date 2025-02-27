def return_nth_smallest_ascii(s):
    substring = s[30:71]
    characters = [c for c in substring if c in s]
    sorted_characters = sorted(characters)
    return sorted_characters[14]