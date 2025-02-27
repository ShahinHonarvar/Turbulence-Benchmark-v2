def all_substring_of_size_n(s):
    length, required_length = (len(s), 120)
    if length < required_length:
        return []
    substrings = set()
    for i in range(length - required_length + 1):
        substring = s[i:i + required_length]
        if len(set(substring)) == required_length:
            substrings.add(substring)
    return list(substrings)