def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, min(len(letters), i + 8)):
            palindrome = ''.join(letters[i:j])
            reversed_palindrome = ''.join(reversed(palindrome))
            if len(palindrome) >= 7 and palindrome.lower() == reversed_palindrome.lower():
                palindromes.add(palindrome)
    return palindromes