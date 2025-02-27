def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def find_palindromes(text, n):
    length = len(text)
    palindromes = set()
    for i in range(length - n + 1):
        substring = text[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes

def palindrome_of_length_n(text):
    return find_palindromes(text, 223)