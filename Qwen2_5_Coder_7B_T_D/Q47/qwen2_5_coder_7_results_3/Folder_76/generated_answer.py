def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    s = s[101:293].lower()
    for start in range(len(s) - 153):
        for length in range(154, 183):
            if is_palindrome(s[start:start + length]):
                result.add(s[start:start + length])
    return result