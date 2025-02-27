def palindromes_of_specific_lengths(s):
    result = set()

    def expand_around_center(left, right):
        while left >= 10 and right <= 100 and (left <= right):
            if s[left:right + 1].isalpha():
                substring = s[left:right + 1].lower()
                if substring == substring[::-1] and 10 <= len(substring) <= 50:
                    result.add(substring)
                left -= 1
                right += 1
            else:
                break
    for i in range(10, 101):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return result