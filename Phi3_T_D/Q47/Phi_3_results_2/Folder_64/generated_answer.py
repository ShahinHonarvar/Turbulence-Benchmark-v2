def palindromes_of_specific_lengths(s):
    s = s[:8].lower()
    result = set()
    chars = 'abcdefghijklmnopqrstuvwxyz'

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]) and (s[left] in chars):
            result.add(s[left:right + 1])
            left -= 1
            right += 1
    for i in range(len(s) - 3):
        expand_around_center(i, i + 3)
    for i in range(len(s) - 2):
        expand_around_center(i, i + 2)
    return result