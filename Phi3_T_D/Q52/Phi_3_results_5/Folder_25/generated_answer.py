def palindrome_of_length_n(s):
    s = s.lower()
    result = set()

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            result.add(s[left:right + 1])
            left -= 1
            right += 1
    for i in range(len(s)):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return {palindrome for palindrome in result if len(palindrome) == 90}