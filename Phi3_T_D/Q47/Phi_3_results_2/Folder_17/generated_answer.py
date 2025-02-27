def palindromes_of_specific_lengths(s):

    def is_valid_char(c):
        return 'a' <= c <= 'z'

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and is_valid_char(s[left]) and is_valid_char(s[right]):
            if left > 22 and right <= 95 and (52 <= right - left <= 55):
                yield s[left:right + 1]
            left -= 1
            right += 1
    s = s[22:96]
    palindromes = set()
    for i in range(26, 50):
        for p in expand_around_center(i, i):
            palindromes.add(p)
    for i in range(26, 50):
        for p in expand_around_center(i - 1, i):
            palindromes.add(p)
    return palindromes