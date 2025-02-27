def palindromes_of_specific_lengths(s):

    def is_valid_palindrome(p):
        return p == p[::-1] and p.isalpha() and p.isascii() and p.islower()
    s = s[20:75].lower()
    result = set()
    for length in range(36, 43):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if is_valid_palindrome(sub):
                result.add(sub)
    return result