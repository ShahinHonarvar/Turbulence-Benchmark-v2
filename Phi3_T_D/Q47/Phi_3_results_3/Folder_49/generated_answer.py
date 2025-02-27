from string import ascii_letters

def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    valid_palindromes = set()
    s = s[10:101]
    s = ''.join((c.lower() if c in ascii_letters else '' for c in s))
    for length in range(10, 51):
        for i in range(len(s) - length + 1):
            if is_palindrome(s[i:i + length]):
                valid_palindromes.add(s[i:i + length])
    return valid_palindromes