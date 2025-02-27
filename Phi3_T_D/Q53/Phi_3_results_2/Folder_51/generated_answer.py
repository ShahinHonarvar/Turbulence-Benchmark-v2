def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def expand(center, left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            yield s[left:right + 1]
            left -= 1
            right += 1

    def find_palindromes(s):
        res = set()
        for i in range(len(s)):
            for palindrome in expand(i, i, i):
                if len(palindrome) >= 63:
                    res.add(palindrome)
            for palindrome in expand(i, i - 1, i):
                if len(palindrome) >= 63:
                    res.add(palindrome)
        return res
    return find_palindromes(s)