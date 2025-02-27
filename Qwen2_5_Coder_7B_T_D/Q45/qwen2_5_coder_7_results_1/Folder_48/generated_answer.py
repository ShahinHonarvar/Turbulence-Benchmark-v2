def palindromes_between_indices(s):
    subset = s[6:9].lower()
    letters = sorted(subset)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            perm = ''.join(letters[i:j])
            if perm == perm[::-1]:
                palindromes.add(perm)
    return palindromes