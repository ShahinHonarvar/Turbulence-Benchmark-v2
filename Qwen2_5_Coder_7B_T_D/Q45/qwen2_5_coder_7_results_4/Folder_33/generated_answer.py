def palindromes_between_indices(s):
    letters = s[7:10]
    letters = ''.join(filter(str.isalpha, letters)).lower()
    if len(letters) < 4:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            substring = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n]
                            if substring == substring[::-1] and len(substring) == 4:
                                palindromes.add(substring)
    return palindromes