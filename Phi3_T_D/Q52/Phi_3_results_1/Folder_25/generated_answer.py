def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = {''.join(x) for x in (s[i:i + 90].lower() for i in range(len(s) - 89)) if x.isalpha() and is_palindrome(x)}
    return palindromes