def palindromes_between_indices(s):
    letters = set(s[3:9].lower())
    if len(letters) < 5:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        word = letters[i] * 2 + letters[j] * 2 + letters[k] * 2 + letters[l] * 2 + letters[m] * 2
                        if word.lower() == word[::-1].lower():
                            palindromes.add(word)
    return palindromes