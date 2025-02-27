def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 91):
        substring = text[i:i + 92]
        if all((c.isalpha() for c in substring)) and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes