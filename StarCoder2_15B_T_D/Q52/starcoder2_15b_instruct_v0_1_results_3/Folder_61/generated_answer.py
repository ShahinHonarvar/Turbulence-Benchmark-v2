def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 73):
        substring = string[i:i + 74]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes