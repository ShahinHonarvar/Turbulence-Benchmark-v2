def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 91):
        current_substring = s[i:i + 92]
        if len(set(current_substring)) == 92:
            substrings.add(current_substring)
    return list(substrings)