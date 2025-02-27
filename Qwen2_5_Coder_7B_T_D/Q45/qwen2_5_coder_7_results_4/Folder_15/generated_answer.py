def palindromes_between_indices(s):
    s = s.lower()
    n = len(s)
    result = set()
    for i in range(1, n - 1):
        for j in range(i + 2, n + 1):
            sub = s[i:j]
            if sub.lower() == sub[::-1].lower():
                result.add(sub)
    return result