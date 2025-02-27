def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            word = ''.join(sorted(letters[i:j] + letters[k:l] + letters[m:n]))
                            if word == word[::-1] and len(word) >= 5:
                                palindromes.add(word)
    return palindromes