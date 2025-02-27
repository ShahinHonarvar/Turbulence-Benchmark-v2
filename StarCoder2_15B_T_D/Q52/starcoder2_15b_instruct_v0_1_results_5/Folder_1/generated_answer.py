def palindrome_of_length_n(string):
    palindromes = set()
    substring_length = 27
    for i in range(len(string) - substring_length + 1):
        substring = string[i:i + substring_length]
        if substring == substring[::-1]:
            if all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes