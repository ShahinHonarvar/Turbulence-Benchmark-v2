def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string) - 49):
        for j in range(i + 49, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes