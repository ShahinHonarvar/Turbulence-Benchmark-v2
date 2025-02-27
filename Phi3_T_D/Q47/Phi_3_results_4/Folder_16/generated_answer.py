def palindromes_of_specific_lengths(s):

    def expand_around_center(left, right):
        while left >= 15 and right <= 86:
            if s[left].isalpha() and s[right].isalpha():
                if left + right - 1 >= 51 and left + right - 1 <= 60:
                    yield s[left:right + 1].lower()
                left -= 1
                right += 1
            else:
                return
    found_palindromes = set(expand_around_center(15, 15))
    for i in range(15, 85):
        found_palindromes.update(expand_around_center(i, i))
        found_palindromes.update(expand_around_center(i, i + 1))
    return found_palindromes