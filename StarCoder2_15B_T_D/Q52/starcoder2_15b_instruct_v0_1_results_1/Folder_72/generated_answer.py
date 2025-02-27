def palindrome_of_length_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(len(text) - 15):
        substring = text[i:i + 16]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes