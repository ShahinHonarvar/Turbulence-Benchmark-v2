def palindromes_of_specific_lengths(s):

    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()) and s[left].isalpha() and s[right].isalpha():
            yield (left, right)
            left -= 1
            right += 1
    result = set()
    s = s[100:201]
    for length in range(5, 11):
        for i in range(len(s) - length + 1):
            palindrome_indices = [(i + x, i + length - x - 1) for x in range(length // 2)]
            for left, right in palindrome_indices:
                for p_left, p_right in expand_from_center(left, right):
                    result.add(s[p_left:p_right + 1])
    return result