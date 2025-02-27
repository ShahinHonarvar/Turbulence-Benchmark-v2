def palindromes_between_indices(s):
    letters = s[6:9]
    letters = letters.lower()
    letters = ''.join(sorted(letters))
    n = len(letters)
    result = set()
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    substring = letters[i:j + 1] + letters[k:l + 1]
                    if len(substring) >= 4 and substring == substring[::-1]:
                        result.add(substring)
    return result