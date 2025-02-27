def palindrome_of_length_n(text):
    n = 338
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes