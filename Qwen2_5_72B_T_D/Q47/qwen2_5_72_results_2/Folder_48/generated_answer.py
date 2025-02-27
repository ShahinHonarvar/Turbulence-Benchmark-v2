def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[155:284]
    s = ''.join(filter(str.isalpha, s.lower()))
    results = set()
    for length in range(104, 121):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                results.add(substring)
    return results