def all_substring_of_size_n(s):
    results = set()
    for i in range(len(s) - 104):
        substring = s[i:i + 105]
        if len(set(substring)) == 105:
            results.add(substring)
    return list(results)