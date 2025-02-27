def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for length in range(30, 47):
        for i in range(26, 85 - length + 1):
            substring = s[i:i + length].lower()
            if set(substring) <= alphabet and is_palindrome(substring):
                result.add(substring)
    return result