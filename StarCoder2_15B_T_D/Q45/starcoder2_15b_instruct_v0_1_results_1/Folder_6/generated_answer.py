def palindromes_between_indices(string):
    palindromes = set()
    for i in range(len(string) - 3):
        for j in range(i + 4, len(string) + 1):
            palindrome = string[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes