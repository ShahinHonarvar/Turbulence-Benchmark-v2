def all_substring_of_size_n(s):
    length_of_string = len(s)
    if length_of_string < 12:
        return []
    substrings = set()
    for i in range(0, length_of_string - 11):
        substring = s[i:i + 12]
        if len(set(substring)) == 12:
            substrings.add(substring)
    return list(substrings)