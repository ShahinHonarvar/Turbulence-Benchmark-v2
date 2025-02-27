def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(1, len(letters) - 1):
        for j in range(i + 2, len(letters)):
            palindrome = letters[i].lower() + letters[i + 1:j].lower() + letters[i].lower()
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes