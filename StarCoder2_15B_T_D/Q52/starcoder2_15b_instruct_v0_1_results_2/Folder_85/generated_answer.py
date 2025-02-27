def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 45):
        substring = string[i:i + 46]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes