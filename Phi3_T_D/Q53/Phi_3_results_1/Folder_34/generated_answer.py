def palindrome_of_length_at_least_n(s):
    s = s.lower()
    N = len(s)
    palindromes = set()

    def expand_around_center(left, right):
        while left >= 0 and right < N and s[left].isalpha() and s[right].isalpha():
            substr = s[left:right + 1]
            if len(substr) >= 68 and substr == substr[::-1]:
                palindromes.add(substr)
            left -= 1
            right += 1
    for i in range(N):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return palindromes