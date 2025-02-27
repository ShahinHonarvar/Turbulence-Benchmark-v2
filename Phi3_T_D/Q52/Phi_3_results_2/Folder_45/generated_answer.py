def palindrome_of_length_n(s):

    def is_palindrome(text):
        return text == text[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 20):
        substring = s[i:i + 21]
        if all((c.isalpha() for c in substring)) and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes