def palindrome_of_length_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text.lower()
    length = len(text)
    palindromes = set()
    for i in range(length - 12):
        substring = text[i:i + 13]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes