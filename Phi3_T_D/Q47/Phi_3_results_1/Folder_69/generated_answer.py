def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1] and all(('a' <= c.lower() <= 'z' for c in substring))
    result_set = set()
    s = s[11:97].lower()
    for length in range(45, 53):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if is_palindrome(substr):
                result_set.add(substr)
    return result_set