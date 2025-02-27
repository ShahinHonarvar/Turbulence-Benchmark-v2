def palindromes_between_indices(s):
    letters = s[3:10].lower()
    if len(letters) < 5:
        return set()
    letters = set(letters)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        word = ''.join(sorted(letters[i] + letters[j] + letters[k] + letters[l] + letters[m]))
                        if word == word[::-1]:
                            palindromes.add(word)
    return palindromes