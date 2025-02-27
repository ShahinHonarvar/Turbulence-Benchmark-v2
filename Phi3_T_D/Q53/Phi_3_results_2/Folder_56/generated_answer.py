from itertools import product

def palindrome_of_length_at_least_n(s):

    def find_palindromes(base, center, left, right):
        if center == 0:
            substr = left + base + right
            if len(substr) >= 84:
                return {substr}
            else:
                return set()
        else:
            palindromes = find_palindromes(base, center - 1, left, right)
            if base[center - 1] == base[center]:
                palindromes |= find_palindromes(base, center - 1, left + base[center - 1], right + base[center - 1])
            return palindromes
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for left_len in range(len(s)):
        for i in range(left_len, min(left_len + 84, len(s))):
            if s[i] in 'aeiou':
                palindromes |= find_palindromes(s[left_len:i + 1], i, '', '')
    return palindromes