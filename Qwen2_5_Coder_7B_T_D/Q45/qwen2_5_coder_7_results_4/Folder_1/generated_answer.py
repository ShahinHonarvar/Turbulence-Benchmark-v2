def palindromes_between_indices(s):
    letters = set(s[4:8].lower())
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        word = ''.join(sorted(letters[i:j] + letters[j:k] + letters[k:l] + letters[l:m] + letters[m:]))
                        if word == word[::-1] and len(word) >= 5:
                            palindromes.add(word)
    return palindromes