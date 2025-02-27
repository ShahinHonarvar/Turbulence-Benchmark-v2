def palindromes_between_indices(string):
    letters = set(string.lower())
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                for d in letters:
                    for e in letters:
                        for f in letters:
                            for g in letters:
                                palindrome = ''.join([a, b, c, d, e, f, g])
                                if palindrome == palindrome[::-1]:
                                    palindromes.add(palindrome)
    return palindromes