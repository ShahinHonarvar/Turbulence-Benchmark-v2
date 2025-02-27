def palindrome_of_length_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(len(text) - 45 + 1):
        substring = text[i:i + 45]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes