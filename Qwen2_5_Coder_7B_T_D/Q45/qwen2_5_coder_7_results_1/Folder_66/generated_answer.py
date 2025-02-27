def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 4, len(letters) + 1):
            perm = ''.join(sorted(letters[i:j]))
            if perm == perm[::-1]:
                palindromes.add(perm)
    return palindromes