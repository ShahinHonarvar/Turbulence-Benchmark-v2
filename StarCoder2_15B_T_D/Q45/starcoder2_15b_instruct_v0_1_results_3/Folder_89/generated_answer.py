def palindromes_between_indices(text):
    letters = [c for c in text if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 5):
        for j in range(i + 5, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes