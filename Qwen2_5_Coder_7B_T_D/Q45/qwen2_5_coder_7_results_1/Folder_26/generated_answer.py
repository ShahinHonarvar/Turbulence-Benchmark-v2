def palindromes_between_indices(s):
    letters = s[4:7].lower()
    length = len(letters)
    if length < 3:
        return set()
    palindromes = set()
    for i in range(length):
        for j in range(i, length):
            for k in range(j, length):
                for l in range(k, length):
                    for m in range(l, length):
                        for n in range(m, length):
                            word = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n]
                            if word == word[::-1]:
                                palindromes.add(word)
    return palindromes