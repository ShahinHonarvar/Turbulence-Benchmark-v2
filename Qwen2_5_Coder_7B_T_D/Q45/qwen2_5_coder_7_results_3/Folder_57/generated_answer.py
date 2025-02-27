def palindromes_between_indices(s):
    s = s[2:6].lower()
    letters = set(s)
    result = set()
    for i in range(len(s)):
        for j in range(i + 5, len(s) + 1):
            sub = ''.join(sorted(s[i:j]))
            if sub == sub[::-1] and len(sub) >= 5:
                result.add(sub)
    return result