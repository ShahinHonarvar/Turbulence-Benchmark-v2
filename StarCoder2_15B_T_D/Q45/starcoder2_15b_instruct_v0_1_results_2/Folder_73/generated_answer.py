def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(3, 7):
        for j in range(len(letters) - i + 1):
            s = letters[j:j + i]
            if s == s[::-1]:
                palindromes.add(''.join(s))
    return palindromes