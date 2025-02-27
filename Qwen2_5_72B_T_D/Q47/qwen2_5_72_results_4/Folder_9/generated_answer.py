def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[:301]
    valid_palindromes = set()
    for length in range(50, 61):
        for start in range(0, 302 - length):
            sub = s[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                valid_palindromes.add(sub)
    return valid_palindromes