def palindrome_of_length_n(string):
    substrings = []
    for i in range(len(string) - 8):
        substring = string[i:i + 9]
        if substring == substring[::-1]:
            substrings.append(substring)
    palindromes = set()
    for substring in substrings:
        if all((ch.isalpha() for ch in substring)):
            palindromes.add(substring)
    return palindromes