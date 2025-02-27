def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(1, len(letters) - 1):
        for j in range(i + 2, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes