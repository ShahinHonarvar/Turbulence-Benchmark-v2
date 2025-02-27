def all_substring_of_size_n(s):
    n = 94
    unique_subs = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            unique_subs.add(substring)
    return list(unique_subs)