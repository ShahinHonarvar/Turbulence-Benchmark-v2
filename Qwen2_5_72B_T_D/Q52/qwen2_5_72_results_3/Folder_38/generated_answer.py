def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    s_length = len(s)
    for i in range(s_length - 37):
        substring = s[i:i + 38]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes