def palindromes_of_specific_lengths(s):
    start, end = (30, 84)
    substr = s[start:end + 1].lower()

    def expand_around_center(left, right):
        palindromes = set()
        while left >= 0 and right < len(substr) and (substr[left] == substr[right]):
            if 12 <= right - left + 1 <= 20 and substr[left:right + 1].isalpha():
                palindromes.add(substr[left:right + 1])
            left -= 1
            right += 1
        return palindromes
    result = set()
    for i in range(len(substr)):
        result |= expand_around_center(i, i)
        result |= expand_around_center(i, i + 1)
    return result