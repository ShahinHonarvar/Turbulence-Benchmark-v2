def palindromes_between_indices(string):
    palindromes = set()
    for i in range(2, len(string) - 1):
        for j in range(i + 1, min(len(string), i + 5) + 1):
            for k in range(j, len(string)):
                palindrome = string[i:j] + string[k]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes