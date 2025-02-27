def palindromes_between_indices(s):
    s = s[3:8].lower()
    letters = set(s)
    if len(letters) < 5:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            substring = ''.join(sorted(letters[i:j] + letters[k:l] + letters[m:n]))
                            if len(substring) >= 5 and substring == substring[::-1]:
                                palindromes.add(substring)
    return palindromes