def all_substring_of_size_n(s):
    n = 110
    s_set = set()
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            s_set.add(substring)
    for item in s_set:
        result.append(item)
    return result