def palindrome_of_length_n(string):
    length = 131
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes