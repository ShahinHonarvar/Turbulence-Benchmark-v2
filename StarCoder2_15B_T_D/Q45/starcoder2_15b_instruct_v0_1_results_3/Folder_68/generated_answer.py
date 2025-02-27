def palindromes_between_indices(string):
    letters = sorted((c for c in string[1:9].lower() if c.isalpha()))
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters)):
            palindrome = letters[i] + letters[i + 1:j][::-1] + letters[j]
            palindromes.add(palindrome)
    return palindromes