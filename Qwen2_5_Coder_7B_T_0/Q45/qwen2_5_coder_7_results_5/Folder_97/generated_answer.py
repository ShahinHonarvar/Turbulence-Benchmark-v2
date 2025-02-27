def palindromes_between_indices(s):
    s = s[:5].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        word = ''.join(sorted(letters[i:j] + letters[k:l] + letters[m:]))
                        if word == word[::-1] and len(word) >= 3:
                            palindromes.add(word)
    return palindromes