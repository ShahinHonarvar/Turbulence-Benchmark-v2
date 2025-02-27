def palindrome_of_length_n(text):
    length = 21
    palindromes = set()
    for i in range(len(text) - length + 1):
        substring = text[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes