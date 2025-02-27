def palindrome_of_length_n(string):
    substrings = set()
    for i in range(len(string) - 56):
        substring = string[i:i + 57]
        if substring == substring[::-1]:
            substrings.add(substring)
    palindromes = set()
    for substring in substrings:
        if all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes