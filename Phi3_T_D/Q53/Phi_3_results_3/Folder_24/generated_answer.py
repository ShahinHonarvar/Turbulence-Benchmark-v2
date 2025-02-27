def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    length = len(text)
    palindromes = set()
    for i in range(length):
        for j in range(i + 53, length + 1):
            substr = text[i:j]
            if all((char.isalpha() for char in substr)) and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes