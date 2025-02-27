def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(1, len(letters) - 1):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i:j + 1][::-1] + letters[i:j]
            if len(palindrome) >= 3:
                palindromes.add(palindrome.lower())
    return palindromes