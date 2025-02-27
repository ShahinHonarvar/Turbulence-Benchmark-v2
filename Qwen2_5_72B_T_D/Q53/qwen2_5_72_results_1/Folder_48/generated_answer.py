def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    n = len(s)
    results = set()
    for center in range(2 * n - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < n and (s[left] == s[right]):
            if right - left + 1 >= 150:
                results.add(s[left:right + 1])
            left -= 1
            right += 1
    return results