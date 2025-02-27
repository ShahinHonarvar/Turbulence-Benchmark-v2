def palindrome_of_length_n(string):
    palindromes = set()
    n = 338
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if all((c.isalpha() for c in substring)):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes