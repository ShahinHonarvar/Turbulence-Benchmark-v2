def palindrome_of_length_at_least_n(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s_lower = s.lower()
    palindromes = set()

    def expand_around_center(left, right):
        while left >= 0 and right < len(s_lower) and (s_lower[left] == s_lower[right]):
            if right - left + 1 >= 90:
                palindromes.add(s_lower[left:right + 1])
            left -= 1
            right += 1
    for i in range(len(s)):
        expand_around_center(i, i)
        if i + 1 < len(s) and s_lower[i] == s_lower[i + 1]:
            expand_around_center(i, i + 1)
    return palindromes