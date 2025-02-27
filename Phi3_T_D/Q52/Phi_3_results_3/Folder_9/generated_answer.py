def palindrome_of_length_n(text):
    length = 72
    lower_text = text.lower()
    set_palindromes = set()
    for i in range(len(text) - length + 1):
        substring = lower_text[i:i + length]
        if substring.isalpha() and substring == substring[::-1]:
            set_palindromes.add(substring.upper())
    return set_palindromes