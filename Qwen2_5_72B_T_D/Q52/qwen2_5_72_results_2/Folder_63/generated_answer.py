def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    n = 18
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr.isalpha() and is_palindrome(substr):
            palindromes.add(substr)
    return palindromes