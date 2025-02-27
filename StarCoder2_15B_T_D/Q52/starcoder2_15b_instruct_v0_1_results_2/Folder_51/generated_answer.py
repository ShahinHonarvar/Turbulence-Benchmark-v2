def palindrome_of_length_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(len(text) - 72):
        substring = text[i:i + 73]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes