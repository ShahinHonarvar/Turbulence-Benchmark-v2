def all_substring_of_size_n(s):
    substrings = set()
    substring_set = set()
    for i in range(len(s) - 72):
        current_substring = s[i:i + 73]
        if len(set(current_substring)) == 73:
            if current_substring not in substring_set:
                substrings.add(current_substring)
                substring_set.add(current_substring)
    return list(substrings)