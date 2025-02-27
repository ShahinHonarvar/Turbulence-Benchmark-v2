def palindromes_of_specific_lengths(s):
    s = s[:301]
    results = set()
    s = s.lower()

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
            if left + right < 50 or left + right > 60:
                break
            left -= 1
            right += 1
        if left + 1 < right and right - left >= 50 and (right - left <= 60):
            results.add(s[left + 1:right])
    for i in range(len(s)):
        expand_around_center(i, i)
        if i + 1 < len(s) and s[i] == s[i + 1]:
            expand_around_center(i, i + 1)
    return results