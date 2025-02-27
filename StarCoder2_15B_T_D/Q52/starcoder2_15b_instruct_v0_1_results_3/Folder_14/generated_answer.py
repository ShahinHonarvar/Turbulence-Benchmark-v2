def palindrome_of_length_n(string):
    string = ''.join((c for c in string.lower() if c.isalpha()))
    palindromes = set()
    for i in range(len(string) - 62):
        substring = string[i:i + 63]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes