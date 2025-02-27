def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]

    def get_palindromes(s):
        s = s.lower()
        for length in range(20, 21 + 1):
            for i in range(12, len(s) - length + 1):
                substr = s[i:i + length]
                if substr.isalpha() and all((c.isalpha() for c in substr)):
                    if is_palindrome(substr):
                        yield substr.lower()
    return set(get_palindromes(text))