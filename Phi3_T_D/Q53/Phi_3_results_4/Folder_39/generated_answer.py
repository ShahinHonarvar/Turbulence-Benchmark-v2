def palindrome_of_length_at_least_n(s):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            if right - left + 1 >= 69:
                yield (left, right)
            left -= 1
            right += 1
    palindromes = set()
    for i in range(len(s)):
        for j in expand_around_center(i, i):
            palindromes.add(s[j[0]:j[1] + 1])
        for j in expand_around_center(i, i + 1):
            palindromes.add(s[j[0]:j[1] + 1])
    return palindromes