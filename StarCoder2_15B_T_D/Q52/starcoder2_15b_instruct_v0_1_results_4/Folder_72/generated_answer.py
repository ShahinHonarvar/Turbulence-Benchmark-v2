def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 15):
        substring = string[i:i + 16]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes