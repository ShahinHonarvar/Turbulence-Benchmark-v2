def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 6, len(letters) + 1):
            substring = letters[i:j]
            palindrome = ''.join(substring + substring[::-1])
            palindromes.add(palindrome)
    return palindromes