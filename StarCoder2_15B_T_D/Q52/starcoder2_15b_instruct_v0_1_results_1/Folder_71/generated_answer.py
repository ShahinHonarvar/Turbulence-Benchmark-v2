def palindrome_of_length_n(string):
    palindromes = set()
    length = len(string)
    for i in range(length - 78 + 1):
        substring = string[i:i + 78]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes