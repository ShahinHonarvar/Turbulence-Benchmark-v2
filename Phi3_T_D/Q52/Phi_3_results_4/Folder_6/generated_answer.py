def palindrome_of_length_n(text):
    length = 474
    palindromes = set()
    text_lower = text.lower()
    for i in range(len(text) - length + 1):
        substring = text_lower[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes