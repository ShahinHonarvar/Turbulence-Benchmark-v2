def palindrome_substrings(s):
    n = len(s)
    palindrome_set = set()

    def expand_around_center(left, right):
        while left >= 0 and right < n and (s[left].lower() == s[right].lower()):
            palindrome_set.add(s[left:right + 1])
            left -= 1
            right += 1
    for i in range(n):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return palindrome_set

def palindrome_of_length_at_least_n(s, n=18):
    return {p for p in palindrome_substrings(s) if len(p) >= n}