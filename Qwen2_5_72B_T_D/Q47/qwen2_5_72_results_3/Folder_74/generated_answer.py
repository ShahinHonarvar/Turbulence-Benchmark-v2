def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    for length in range(12, 21):
        for start in range(30, 85 - length + 1):
            substr = s[start:start + length]
            if substr.isalpha() and is_palindrome(substr):
                result.add(substr)
    return result