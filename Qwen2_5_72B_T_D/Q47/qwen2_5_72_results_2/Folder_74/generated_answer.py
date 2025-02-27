def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[30:85]
    result = set()
    for length in range(12, 21):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                result.add(substring)
    return result