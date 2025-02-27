def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 9):
        substring = text[i:i + 10]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes