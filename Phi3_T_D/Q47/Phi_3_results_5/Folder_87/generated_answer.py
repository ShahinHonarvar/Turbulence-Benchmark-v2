from collections import defaultdict

def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    s = s[11:94].lower()
    letter_map = defaultdict(int)
    for start in range(11, 93 - 33):
        for length in range(34, 55):
            if start + length <= 93:
                substring = s[start:start + length]
                if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes