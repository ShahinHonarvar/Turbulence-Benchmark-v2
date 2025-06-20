def palindromes_between_indices(s):
    s = s[4:8].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    word = letters[i] + letters[j] + letters[k] + letters[l]
                    if word == word[::-1] and len(word) >= 4:
                        palindromes.add(word)
    return palindromes