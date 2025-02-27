def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 68 <= len(s):
            current_substring = s[i:i + 68]
            if len(set(current_substring)) == 68:
                substrings.add(current_substring)
    return list(substrings)