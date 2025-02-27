def all_substring_of_size_n(s):
    length = 43
    if length > len(s):
        return []
    seen = set()
    result = []
    for i in range(len(s) - length + 1):
        substring = ''.join(sorted(s[i:i + length]))
        if substring not in seen:
            seen.add(substring)
            result.append(substring)
    return result