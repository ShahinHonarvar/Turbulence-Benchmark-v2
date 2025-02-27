def all_substring_of_size_n(s):
    substrings = set()
    length = 89
    seen = set()
    for i in range(len(s) - length + 1):
        if i == 0 or s[i - 1] not in s[i:i + length]:
            if length == len(set(s[i:i + length])):
                substrings.add(s[i:i + length])
    return list(substrings)