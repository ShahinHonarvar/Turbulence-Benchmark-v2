def palindrome_of_length_at_least_n(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = s.lower()
    result = set()
    for start in range(len(s)):
        for length in range(32, len(s) - start + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                result.add(substring)
    return result