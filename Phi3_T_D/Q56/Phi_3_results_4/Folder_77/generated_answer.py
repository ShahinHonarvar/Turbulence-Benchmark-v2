def all_substring_of_size_n(s):
    n = 144
    seen = set()
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            if substring not in seen:
                seen.add(substring)
                result.append(substring)
    return result