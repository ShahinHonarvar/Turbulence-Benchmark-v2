def palindrome_of_length_n(text):
    palindromes = set()
    text = text.lower()
    for i in range(len(text) - 185):
        substring = text[i:i + 186]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes