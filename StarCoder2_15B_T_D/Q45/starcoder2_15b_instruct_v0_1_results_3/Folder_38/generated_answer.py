def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(3, len(string) - 4):
        for j in range(i + 5, len(string)):
            palindrome = string[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes