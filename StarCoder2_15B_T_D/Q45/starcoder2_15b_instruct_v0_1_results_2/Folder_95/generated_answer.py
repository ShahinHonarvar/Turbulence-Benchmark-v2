def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 3, len(letters) + 1):
            for k in range(i + 1, j):
                palindrome = letters[i:k] + letters[k:i:-1]
                if len(palindrome) >= 3:
                    palindromes.add(''.join(palindrome).lower())
    return palindromes