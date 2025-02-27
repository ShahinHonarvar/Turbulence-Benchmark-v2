def palindromes_of_specific_lengths(s):
    start, end = (26, min(84, len(s)))

    def expand(left, right):
        while left >= start and right <= end and (s[left].lower() == s[right].lower()):
            if right - left >= 3 and right - left <= 46:
                yield s[left:right + 1]
            left -= 1
            right += 1
    result = set()
    for center in range(start, end + 1):
        result.update(expand(center - 1, center))
        result.update(expand(center, center + 1))
    return set(filter(str.isalpha, result))