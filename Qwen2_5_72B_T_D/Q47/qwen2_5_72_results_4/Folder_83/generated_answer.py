def palindromes_of_specific_lengths(s):

    def is_palindrome(v):
        return v == v[::-1]
    s = s[75:96].lower()
    result = set()
    for length in range(7, 10):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result