def palindromes_of_specific_lengths(s):

    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()) and s[left].isalpha():
            yield s[left:right + 1]
            left -= 1
            right += 1
    s = s[65:99 + 1]
    result_set = set()
    for i in range(65, 99):
        for span in (expand_from_center(i, i + j) for j in range(26 - i, 34 - i)):
            for p in span:
                if 25 < len(p) <= 33:
                    result_set.add(p)
    return result_set