def all_substring_of_size_n(s):
    n = 41
    result = []
    substring_set = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in substring_set:
            result.append(substring)
            substring_set.add(substring)
    return result