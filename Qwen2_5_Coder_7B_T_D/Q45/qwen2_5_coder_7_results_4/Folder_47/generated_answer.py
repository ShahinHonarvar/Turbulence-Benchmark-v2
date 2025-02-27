def palindromes_between_indices(s):
    letters = s[3:8].lower()
    unique_letters = set(letters)
    if len(unique_letters) < 5:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        word = letters[i] + letters[j] + letters[k] + letters[l] + letters[m]
                        if word == word[::-1]:
                            palindromes.add(word)
    return palindromes