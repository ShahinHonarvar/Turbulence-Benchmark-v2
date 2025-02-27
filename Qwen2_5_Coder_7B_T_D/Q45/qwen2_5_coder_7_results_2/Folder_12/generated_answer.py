def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = set(s)
    if len(letters) < 2:
        return set()
    result = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub = ''.join(sorted(s[i:j]))
            if sub == sub[::-1]:
                result.add(sub)
    return result