def palindromes_between_indices(s):
    letters = s[2:9].lower()
    letters_set = set(letters)
    palindromes = set()
    for i in range(len(letters_set)):
        for j in range(i, len(letters_set)):
            for k in range(j, len(letters_set)):
                for l in range(k, len(letters_set)):
                    for m in range(l, len(letters_set)):
                        for n in range(m, len(letters_set)):
                            word = letters_set[i] * 2 + letters_set[j] * 2 + letters_set[k] * 2 + letters_set[l] * 2 + letters_set[m] * 2 + letters_set[n] * 2
                            if word == word[::-1] and len(word) >= 6:
                                palindromes.add(word)
    return palindromes