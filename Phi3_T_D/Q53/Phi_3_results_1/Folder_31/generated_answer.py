def palindrome_of_length_at_least_n(s):

    def expand_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            count += 1
            left -= 1
            right += 1
        return count
    palindromes = set()
    for i in range(len(s)):
        length = expand_around_center(i, i)
        if length >= 34:
            palindromes.add(s[i - length + 1:i + length // 2 + 1])
        length = expand_around_center(i, i + 1)
        if length >= 34 - 1:
            palindromes.add(s[i - length // 2:i + length // 2 + 1])
    return palindromes