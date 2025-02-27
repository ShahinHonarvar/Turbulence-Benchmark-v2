def palindromes_between_indices(s):
    letters = [c for c in s[2:7] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes