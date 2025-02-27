def palindrome_of_length_n(text):
    palindromes = set()
    text_lower = text.lower()
    for i in range(len(text_lower) - 25):
        substring = text_lower[i:i + 25]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes