def all_substring_of_size_n(s):
    length, found = (len(s), set())
    if length < 18:
        return []
    for i in range(length - 17):
        substring = s[i:i + 18]
        if len(set(substring)) == 18:
            found.add(substring)
    return list(found)