def palindrome_of_length_at_least_n(s):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
            if s[left].lower() == s[right].lower():
                yield s[left:right + 1]
            else:
                break
            left -= 1
            right += 1
    palindromes = set()
    for i in range(len(s)):
        for palindrome in expand_around_center(i, i):
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
        for palindrome in expand_around_center(i, i + 1):
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes