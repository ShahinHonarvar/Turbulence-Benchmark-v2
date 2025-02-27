def palindromes_between_indices(s):
    letters = s[2:5]
    letters = letters.lower()
    letters = set(letters)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        word = ''.join(sorted([letters[i], letters[j], letters[k], letters[l], letters[m]]))
                        if word == word[::-1] and len(word) >= 4:
                            palindromes.add(word)
    return palindromes