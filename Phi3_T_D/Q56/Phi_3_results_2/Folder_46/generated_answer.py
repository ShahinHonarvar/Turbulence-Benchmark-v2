def all_substring_of_size_n(s):
    n = len(s)
    substrings = set()
    for i in range(n - 86):
        temp_substring = s[i:i + 87]
        if len(set(temp_substring)) == 87:
            substrings.add(temp_substring)
    return list(substrings)