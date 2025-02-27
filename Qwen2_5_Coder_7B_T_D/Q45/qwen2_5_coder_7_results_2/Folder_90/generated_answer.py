def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = set(s)
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                for d in letters:
                    for e in letters:
                        for f in letters:
                            word = a + b + c + d + e + f
                            if word == word[::-1] and len(word) >= 4:
                                palindromes.add(word)
    return palindromes