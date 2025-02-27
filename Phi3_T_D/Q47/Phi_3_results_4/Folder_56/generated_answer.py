def is_english_letter(c):
    return c.isalpha() and c.lower() in 'abcdefghijklmnopqrstuvwxyz'

def expand_around_center(s, l, r):
    while l >= 1 and r <= 9 and is_english_letter(s[l]) and is_english_letter(s[r - 1]):
        if s[l:r] == s[l:r][::-1] and 3 <= r - l <= 7:
            yield s[l:r]
        l -= 1
        r += 1

def palindromes_of_specific_lengths(s):
    pali_set = set()
    for i in range(1, 10):
        for j in range(i, min(i + 8, 10)):
            for palindrome in expand_around_center(s, i, j):
                pali_set.add(palindrome)
    return pali_set