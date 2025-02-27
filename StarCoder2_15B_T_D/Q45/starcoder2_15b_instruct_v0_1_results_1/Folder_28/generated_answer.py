def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(1, len(letters) - 1):
        for j in range(i + 2, len(letters)):
            palindrome = letters[i:j + 1][::-1] + letters[i + 1:j][::-1] + letters[i]
            palindromes.add(palindrome)
    return palindromes