def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 6):
        for j in range(i + 5, len(string)):
            palindrome = string[i:j + 1]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes