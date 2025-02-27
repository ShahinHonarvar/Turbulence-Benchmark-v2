def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 474 + 1):
        substring = string[i:i + 474]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes