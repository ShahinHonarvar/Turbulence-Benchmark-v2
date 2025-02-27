def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 256):
        substring = string[i:i + 257]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes