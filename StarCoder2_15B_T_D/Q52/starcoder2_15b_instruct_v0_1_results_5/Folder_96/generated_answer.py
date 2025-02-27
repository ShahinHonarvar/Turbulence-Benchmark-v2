def palindrome_of_length_n(string):
    length = 83
    palindromes = set()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring == substring[::-1]:
            if all((ch.isalpha() for ch in substring)):
                palindromes.add(substring)
    return palindromes