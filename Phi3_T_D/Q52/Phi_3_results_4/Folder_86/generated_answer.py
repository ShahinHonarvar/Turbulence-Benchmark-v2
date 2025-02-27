def palindrome_of_length_n(text):
    length = 181
    text_lower = text.lower()
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(len(text_lower) - length + 1):
        substring = text_lower[i:i + length]
        if is_palindrome(substring):
            palindromes.add(text_lower[i:i + length])
    return palindromes