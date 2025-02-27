def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    length = 49
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if substr.isalpha() and is_palindrome(substr):
            palindromes.add(substr)
    return palindromes