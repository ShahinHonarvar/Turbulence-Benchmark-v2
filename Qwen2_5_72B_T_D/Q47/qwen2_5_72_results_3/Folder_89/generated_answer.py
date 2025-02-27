def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[18:89]
    result = set()
    for length in range(12, 15):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub.lower())
    return result