def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(2, len(letters) - 2 + 1):
        for j in range(i + 2, len(letters)):
            palindrome = letters[i].lower() + letters[i + 1].lower() + letters[j].lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes