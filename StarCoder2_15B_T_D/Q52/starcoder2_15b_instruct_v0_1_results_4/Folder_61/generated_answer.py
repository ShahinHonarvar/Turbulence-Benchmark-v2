def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 74 + 1):
        substring = text[i:i + 74]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes