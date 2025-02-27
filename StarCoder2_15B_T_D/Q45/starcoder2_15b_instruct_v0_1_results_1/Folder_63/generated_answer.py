def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(0, len(string) - 2):
        for j in range(i + 1, len(string)):
            for k in range(j + 1, len(string)):
                palindrome = string[i] + string[j] + string[k]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes