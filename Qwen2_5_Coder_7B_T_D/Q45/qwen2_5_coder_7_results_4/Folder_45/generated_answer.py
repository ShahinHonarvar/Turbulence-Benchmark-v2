def palindromes_between_indices(s):
    letters = set(s[5:10].lower())
    if len(letters) < 2:
        return set()
    palindromes = set()
    for a in letters:
        for b in letters:
            if a != b:
                for c in letters:
                    for d in letters:
                        if a != c and b != d:
                            word = a + b + c + d + d + c + b + a
                            if word == word[::-1]:
                                palindromes.add(word)
    return palindromes