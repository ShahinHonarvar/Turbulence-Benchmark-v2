def palindromes_between_indices(s):
    letters = s[1:4].lower()
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(i, len(letters)):
                for l in range(i, len(letters)):
                    for m in range(i, len(letters)):
                        for n in range(i, len(letters)):
                            word = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n]
                            if word == word[::-1] and len(word) >= 4:
                                palindromes.add(word)
    return palindromes