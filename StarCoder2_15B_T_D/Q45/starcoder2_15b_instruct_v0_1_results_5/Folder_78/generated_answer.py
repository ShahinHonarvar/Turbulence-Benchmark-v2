def palindromes_between_indices(string):
    letters = [c for c in string[6:9].lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters)):
            palindrome = letters[i] + letters[i + 1] + letters[j]
            if palindrome not in palindromes:
                palindromes.add(palindrome)
    return palindromes