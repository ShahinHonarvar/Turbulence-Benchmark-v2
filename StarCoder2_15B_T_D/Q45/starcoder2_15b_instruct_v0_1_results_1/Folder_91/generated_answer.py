def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, min(len(letters), i + 6) + 1):
            palindrome = ''.join(letters[i:j])
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes