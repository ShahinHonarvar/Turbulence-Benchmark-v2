def palindromes_between_indices(s):
    letters = set(s[4:6].lower())
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(len(letters)):
                    for m in range(len(letters)):
                        for n in range(len(letters)):
                            word = ''.join([letters[i], letters[j], letters[k], letters[l], letters[m], letters[n]])
                            if word == word[::-1] and len(word) >= 3:
                                palindromes.add(word)
    return palindromes