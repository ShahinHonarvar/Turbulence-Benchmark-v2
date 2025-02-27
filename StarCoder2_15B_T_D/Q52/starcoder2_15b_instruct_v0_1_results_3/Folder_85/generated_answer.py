def palindrome_of_length_n(text):
    n = 46
    palindromes = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes