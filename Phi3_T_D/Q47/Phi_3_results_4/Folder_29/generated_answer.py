from collections import Counter

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = ''.join([c for c in s[15:95] if c.isalpha()]).lower()
    palindrome_set = set()
    for i in range(18, 74):
        for start_index in range(len(substring) - i + 1):
            candidate = substring[start_index:start_index + i]
            if is_palindrome(candidate):
                palindrome_set.add(candidate)
    return palindrome_set