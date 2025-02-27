def palindromes_between_indices(s):
    letters = [c for c in s[2:5] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters)):
            palindrome = ''.join([letters[i], *letters[i + 1:j], letters[i]])
            palindromes.add(palindrome)
    return palindromes