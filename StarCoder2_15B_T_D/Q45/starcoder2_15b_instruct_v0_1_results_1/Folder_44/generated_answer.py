def palindromes_between_indices(string):
    string = ''.join((c for c in string if c.isalpha())).lower()
    palindromes = set()
    for i in range(2, 8):
        for j in range(i + 1, 8):
            palindrome = string[i:j + 1]
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes