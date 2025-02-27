def all_substring_of_size_n(s):
    if len(s) < 142:
        return []
    unique_substrings = set()
    for i in range(len(s) - 141):
        current_substring = s[i:i + 142]
        if len(set(current_substring)) == 142:
            unique_substrings.add(current_substring)
    return list(unique_substrings)