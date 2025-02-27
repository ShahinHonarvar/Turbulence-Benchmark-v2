def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text.lower()
    palindrome_set = set()
    n = 81
    for i in range(len(text)):
        for j in range(i + n, len(text) + 1):
            substring = text[i:j]
            if is_palindrome(substring) and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set