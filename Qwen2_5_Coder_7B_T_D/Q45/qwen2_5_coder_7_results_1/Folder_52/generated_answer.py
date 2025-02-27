def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for m in range(l + 1, len(letters)):
                        for n in range(m + 1, len(letters)):
                            for o in range(n + 1, len(letters)):
                                word = ''.join(sorted(letters[i:j] + letters[k:l] + letters[m:n] + letters[o:]))
                                if word == word[::-1] and len(word) >= 6:
                                    palindromes.add(word)
    return palindromes