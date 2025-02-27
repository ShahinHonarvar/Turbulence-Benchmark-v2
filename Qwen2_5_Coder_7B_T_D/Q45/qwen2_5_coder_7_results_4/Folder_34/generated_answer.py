def palindromes_between_indices(s):
    substr = s[5:8].lower()
    letters = sorted(substr)
    n = len(letters)
    palindromes = set()
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                perm = ''.join(letters[i:j + 1] + letters[k:] + letters[i:k])
                if perm == perm[::-1] and len(perm) >= 4:
                    palindromes.add(perm)
    return palindromes