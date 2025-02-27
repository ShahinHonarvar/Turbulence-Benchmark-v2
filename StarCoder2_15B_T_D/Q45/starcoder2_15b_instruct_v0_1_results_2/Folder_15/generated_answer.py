def palindromes_between_indices(s):
    s = s.lower()
    result = set()
    for i in range(1, len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                result.add(s[i:j + 1])
    return result