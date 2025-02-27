def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 188 + 1):
        substring = string[i:i + 188]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes