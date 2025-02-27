def palindrome_of_length_at_least_n(s):

    def is_letter(c):
        return 'a' <= c.lower() <= 'z'

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and is_letter(s[left]) and is_letter(s[right]):
            if s[left] == s[right]:
                yield (left, right)
            if right - left + 1 < 96:
                return
            if s[left + 1] == s[right] and left + 1 >= 0 and (right - 1 < len(s)):
                yield (left + 1, right - 1)
            left -= 1
            right += 1
    palindromes = set()
    for i in range(len(s)):
        for left, right in expand_around_center(i, i):
            for left, right in expand_around_center(i, i + 1):
                palindrome = s[left:right + 1]
                if len(palindrome) >= 96:
                    palindromes.add(palindrome.lower())
    return palindromes