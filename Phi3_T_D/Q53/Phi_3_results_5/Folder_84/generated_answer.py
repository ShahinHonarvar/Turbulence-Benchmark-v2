def expand_around_center(s, l, r, direction):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        l -= 1
        r += 1
    return s[l + 1:r]

def palindrome_of_length_at_least_n(string):
    upper_limit = 81
    lower_limit = 0
    palindromes = set()
    for i in range(len(string)):
        single_char = expand_around_center(string, i, i, 0)
        if len(single_char) >= upper_limit:
            palindromes.add(single_char)
        double_char = expand_around_center(string, i, i + 1, 0)
        if len(double_char) >= upper_limit:
            palindromes.add(double_char)
    return palindromes