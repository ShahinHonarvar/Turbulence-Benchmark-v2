def palindrome_of_length_n(string):
    string = string.lower()
    length = len(string)
    palindromes = set()
    for i in range(length - 90):
        substring = string[i:i + 91]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes