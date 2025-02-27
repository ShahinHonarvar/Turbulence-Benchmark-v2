def palindrome_of_length_n(s):
    substrings = set()
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if substring == substring[::-1]:
            substrings.add(substring)
    palindromes = set()
    for substring in substrings:
        if all((ch.isalpha() for ch in substring)):
            palindromes.add(substring)
    return palindromes