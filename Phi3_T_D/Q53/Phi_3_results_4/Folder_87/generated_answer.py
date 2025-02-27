def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for length in range(18, len(text) + 1):
        for i in range(len(text) - length + 1):
            substring = text[i:i + length]
            if 'a' <= substring[0] <= 'z' and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes