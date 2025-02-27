def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 76):
        substr = s[i:i + 77]
        if substr.isalpha():
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes