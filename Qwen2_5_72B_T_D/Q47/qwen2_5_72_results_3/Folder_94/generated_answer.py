def palindromes_of_specific_lengths(s):

    def is_palindrome(p):
        return p == p[::-1] and p.lower() == p[::-1].lower()
    s = s[40:95]
    result = set()
    for length in range(45, 52):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result