def palindromes_between_indices(s):
    s = s[1:5].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for m in range(l + 1, len(letters)):
                        perm = ''.join(sorted(letters[i] + letters[j] + letters[k] + letters[l] + letters[m]))
                        if perm == perm[::-1]:
                            palindromes.add(perm)
    return palindromes