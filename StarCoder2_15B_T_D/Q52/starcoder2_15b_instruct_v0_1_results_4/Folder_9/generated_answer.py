def palindrome_of_length_n(string):
    string = string.lower()
    length = len(string)
    palindromes = set()
    for i in range(length - 72 + 1):
        substring = string[i:i + 72]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes