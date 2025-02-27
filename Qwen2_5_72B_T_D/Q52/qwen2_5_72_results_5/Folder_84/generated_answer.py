def palindrome_of_length_n(text):
    text = text.lower()
    length = 131
    n = len(text)
    palindromes = set()
    for i in range(n - length + 1):
        substring = text[i:i + length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes