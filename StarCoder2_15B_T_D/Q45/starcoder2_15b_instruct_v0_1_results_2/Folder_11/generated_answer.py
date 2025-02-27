def palindromes_between_indices(s):
    letters = [c for c in s[3:8] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i].lower() + letters[j].lower()
            palindromes.add(palindrome)
            palindrome = letters[j].lower() + letters[i].lower()
            palindromes.add(palindrome)
    return palindromes