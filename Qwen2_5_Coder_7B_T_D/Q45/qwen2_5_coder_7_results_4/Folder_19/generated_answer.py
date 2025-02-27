def palindromes_between_indices(s):
    s = s[1:8].lower()
    chars = set(s)
    if len(chars) < 7:
        return set()
    palindromes = set()
    for a in chars:
        for b in chars:
            for c in chars:
                for d in chars:
                    for e in chars:
                        for f in chars:
                            for g in chars:
                                word = a + b + c + d + e + f + g
                                if word == word[::-1]:
                                    palindromes.add(word)
    return palindromes