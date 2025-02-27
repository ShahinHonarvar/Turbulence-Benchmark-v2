def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    n = 93
    s_length = len(s)
    palindromes = set()
    for i in range(s_length - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes