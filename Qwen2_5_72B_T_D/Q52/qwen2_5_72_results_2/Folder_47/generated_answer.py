def palindrome_of_length_n(text):
    text = text.lower()
    length = 34
    palindromes = set()
    for i in range(len(text) - length + 1):
        substring = text[i:i + length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes