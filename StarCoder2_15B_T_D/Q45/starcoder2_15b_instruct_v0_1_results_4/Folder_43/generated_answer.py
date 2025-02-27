def palindromes_between_indices(string):
    string = ''.join((c for c in string if c.isalnum()))
    palindromes = set()
    for i in range(len(string) - 3):
        for j in range(i + 4, len(string) + 1):
            palindrome = string[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes