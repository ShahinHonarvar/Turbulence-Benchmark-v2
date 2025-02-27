def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            yield s[left:right + 1]
            left -= 1
            right += 1

    def find_palindromes(s):
        result = set()
        for i in range(len(s)):
            for palindrome in expand_around_center(i, i):
                if len(palindrome) >= 59:
                    result.add(palindrome)
            for palindrome in expand_around_center(i, i + 1):
                if len(palindrome) >= 59:
                    result.add(palindrome)
        return result
    return find_palindromes(s)