def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]

    def sliding_window(s, window_size):
        for i in range(len(s) - window_size + 1):
            yield s[i:i + window_size]
    palindromes = set()
    for substring in sliding_window(s, 94):
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes