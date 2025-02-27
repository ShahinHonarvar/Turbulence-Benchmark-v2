def palindromes_between_indices(s):
    s = s[2:7].lower()
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i + 2, n + 1):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result