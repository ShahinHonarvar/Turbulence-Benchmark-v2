def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(3, 7):
        for j in range(len(letters) - i + 1):
            s = ''.join(letters[j:j + i]).lower()
            if s == s[::-1]:
                palindromes.add(s)
    return palindromes