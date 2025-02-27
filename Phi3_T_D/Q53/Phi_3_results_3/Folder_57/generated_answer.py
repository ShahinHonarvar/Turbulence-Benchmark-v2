def expand_around_center(s, l, r, pivot):
    length = len(s)
    while l >= 0 and r < length and (s[l].lower() == s[r].lower()):
        l, r = (l - 1, r + 1)
    return s[l + 1:r].lower()

def palindrome_of_length_at_least_n(s):
    length = len(s)
    palindromes = set()
    for pivot in range(length):
        temp = expand_around_center(s, pivot, pivot, pivot)
        if len(temp) >= 93:
            palindromes.add(temp)
        temp = expand_around_center(s, pivot, pivot + 1, pivot)
        if len(temp) >= 93:
            palindromes.add(temp)
    return palindromes