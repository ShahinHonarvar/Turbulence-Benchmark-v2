def palindromes_of_specific_lengths(s):
    result = set()
    if len(s) < 13 or s[10:56] == '':
        return result

    def is_palindrome(subs):
        return subs == subs[::-1]
    for length in range(3, 8):
        for i in range(10, 56 - length + 1):
            substr = s[i:i + length].lower()
            if substr.isalpha() and is_palindrome(substr):
                result.add(substr)
    return result