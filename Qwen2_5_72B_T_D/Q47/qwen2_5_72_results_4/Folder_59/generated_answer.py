def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[:101].lower()
    palindrome_set = set()
    for length in range(3, 16):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if substr.isalpha() and is_palindrome(substr):
                palindrome_set.add(substr)
    return palindrome_set