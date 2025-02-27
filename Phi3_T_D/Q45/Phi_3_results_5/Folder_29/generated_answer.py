def palindromes_between_indices(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = set(s[2:10].lower()) & set(alphabet)
    palindromes = set()
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                for d in alphabet:
                    for e in alphabet:
                        for f in alphabet:
                            candidate = a + b + c + d + e + f
                            if candidate.lower() in letters:
                                palindromes.add(candidate)
    return palindromes