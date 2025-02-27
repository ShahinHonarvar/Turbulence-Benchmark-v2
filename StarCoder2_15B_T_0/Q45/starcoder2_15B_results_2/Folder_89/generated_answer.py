def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 5):
        for j in range(i + 5, len(letters) - 1):
            palindrome = ''.join(letters[i:j + 1])
            if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes