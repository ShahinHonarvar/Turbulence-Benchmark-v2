from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    memo = defaultdict(set)
    n = len(s)
    for center in range(2 * n - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < n and (s[left] == s[right]):
            if right - left + 1 >= 89:
                memo[s[left:right + 1]].add(s[left:right + 1])
            left -= 1
            right += 1
    return set().union(*memo.values())