def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text[32:72].lower()
    result = set()
    for length in range(21, 33):
        for start in range(len(text) - length + 1):
            substr = text[start:start + length]
            if substr.isalpha() and is_palindrome(substr):
                result.add(substr)
    return result