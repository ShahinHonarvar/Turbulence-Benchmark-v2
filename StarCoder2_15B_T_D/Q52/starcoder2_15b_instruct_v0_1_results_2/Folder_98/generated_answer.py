def palindrome_of_length_n(string):
    substrings = []
    for i in range(len(string) - 5):
        for j in range(i + 6, len(string) + 1):
            substring = string[i:j]
            if len(substring) == 6 and substring == substring[::-1]:
                substrings.append(substring)
    palindromes = []
    for substring in substrings:
        if all((ch.isalpha() for ch in substring)):
            palindromes.append(substring)
    return set(palindromes)