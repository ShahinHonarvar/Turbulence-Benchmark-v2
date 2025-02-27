def palindrome_of_length_n(string):
    substrings = [string[i:i + 116] for i in range(len(string) - 115)]
    palindromes = set()
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes