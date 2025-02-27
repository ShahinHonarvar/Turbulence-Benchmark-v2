def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 48):
        substring = string[i:i + 49]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes