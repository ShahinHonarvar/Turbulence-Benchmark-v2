def palindrome_of_length_n(text):
    text = text.lower()
    n = 223
    palindromes = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes