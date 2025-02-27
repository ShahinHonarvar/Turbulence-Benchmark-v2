def palindrome_of_length_at_least_n(s):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            if right - left + 1 >= 122:
                yield s[left:right + 1]
            left -= 1
            right += 1
    all_palindromes = set()
    s_lower = s.lower()
    for i in range(len(s)):
        for palindrome in expand_around_center(i, i):
            all_palindromes.add(palindrome)
        for palindrome in expand_around_center(i, i + 1):
            all_palindromes.add(palindrome)
    return all_palindromes