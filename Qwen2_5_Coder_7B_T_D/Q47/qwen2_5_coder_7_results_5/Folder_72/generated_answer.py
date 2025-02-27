def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    result = set()
    for length in range(27, 59):
        for start in range(26, 91 - length):
            substring = s[start:start + length]
            if is_palindrome(substring):
                result.add(substring)
    return result