def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(4, len(string) - 4):
        for j in range(i + 5, len(string) - 3):
            palindrome = string[i:j + 1]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes