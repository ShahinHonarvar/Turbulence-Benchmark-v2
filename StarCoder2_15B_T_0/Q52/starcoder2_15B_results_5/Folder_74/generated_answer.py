def palindrome_of_length_n(string):
    n = 96
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            if all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes