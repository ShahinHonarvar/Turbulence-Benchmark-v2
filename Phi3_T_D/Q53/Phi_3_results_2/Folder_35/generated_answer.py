def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    length = 26
    palindromes = set()
    for i in range(len(text) - length + 1):
        substring = text[i:i + length]
        if is_palindrome(substring):
            palindromes.add(substring.capitalize())
    return palindromes