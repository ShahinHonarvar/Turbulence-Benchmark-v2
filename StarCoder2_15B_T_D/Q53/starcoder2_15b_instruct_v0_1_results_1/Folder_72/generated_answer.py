def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string) - 88):
        for j in range(i + 88, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes