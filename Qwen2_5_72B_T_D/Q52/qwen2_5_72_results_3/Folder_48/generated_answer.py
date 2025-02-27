def palindrome_of_length_n(text):
    text = text.lower()
    n = 186
    length = len(text)
    palindromes = set()
    for i in range(length - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes