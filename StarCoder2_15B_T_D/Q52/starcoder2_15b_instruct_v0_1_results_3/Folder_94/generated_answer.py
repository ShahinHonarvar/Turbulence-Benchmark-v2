def palindrome_of_length_n(string):
    substrings = set()
    n = 93
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            substrings.add(substring)
    palindromes = set()
    for substring in substrings:
        if all((ch.isalpha() for ch in substring)):
            palindromes.add(substring)
    return palindromes