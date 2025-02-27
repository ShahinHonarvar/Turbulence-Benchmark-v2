def palindrome_of_length_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    text_lower = text.lower()
    for i in range(len(text_lower) - 53):
        substring = text_lower[i:i + 54]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes