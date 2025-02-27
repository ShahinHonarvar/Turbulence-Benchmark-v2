def palindrome_of_length_n(string):
    n = 318
    substrings = [string[i:i + n] for i in range(len(string) - n + 1)]
    palindromes = set()
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes