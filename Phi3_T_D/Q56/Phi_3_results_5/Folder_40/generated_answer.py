def all_substring_of_size_n(s):
    seen = set()
    result = set()
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            substring = s[i:i + 2]
            if substring not in seen:
                seen.add(substring)
                result.add(substring)
    return list(result)