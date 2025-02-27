def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 46):
        substring = string[i:i + 47]
        if substring == substring[::-1]:
            if all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes