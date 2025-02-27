def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 392 + 1):
        substring = string[i:i + 392]
        if substring == substring[::-1]:
            if all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes