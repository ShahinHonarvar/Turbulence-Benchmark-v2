def palindromes_between_indices(s):
    letters = set(s[3:6].lower())
    if len(letters) < 3:
        return set()
    palindromes = set()
    for a in letters:
        for b in letters:
            if a != b:
                for c in letters:
                    palindrome = a + b + c
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes