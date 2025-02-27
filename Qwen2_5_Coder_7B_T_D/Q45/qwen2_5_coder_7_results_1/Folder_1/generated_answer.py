def palindromes_between_indices(s):
    letters = s[4:8].lower()
    letters = set(letters)
    if len(letters) < 3:
        return set()
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                for d in letters:
                    for e in letters:
                        palindrome = a + b + c + d + e
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes