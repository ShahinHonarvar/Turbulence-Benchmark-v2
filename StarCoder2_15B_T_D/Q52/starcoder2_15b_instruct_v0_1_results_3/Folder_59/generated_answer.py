def palindrome_of_length_n(string):
    string = ''.join((c for c in string.lower() if c.isalpha()))
    n = 39
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes