def all_substring_of_size_n(s):
    result = set()
    length_s = len(s)
    if length_s < 142:
        return list(result)
    for i in range(length_s - 141):
        substring = s[i:i + 142]
        if len(set(substring)) == 142:
            result.add(substring)
    return list(result)