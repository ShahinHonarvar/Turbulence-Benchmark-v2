def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(text):
    text_lower = text.lower()
    palindromes = set()
    for i in range(len(text_lower)):
        for j in range(i + 38, len(text_lower) + 1):
            substring = text_lower[i:j]
            if is_palindrome(substring):
                palindromes.add(text_lower[i:j])
    return palindromes if palindromes else set()