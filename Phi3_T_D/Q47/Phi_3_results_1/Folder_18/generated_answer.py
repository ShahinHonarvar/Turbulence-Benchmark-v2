def palindromes_of_specific_lengths(s):
    substring = s[11:84].lower()
    matched_palindromes = set()

    def expand_around_center(left, right):
        while left >= 0 and right < len(substring) and substring[left].isalpha() and substring[right].isalpha():
            if substring[left] == substring[right]:
                matched_palindromes.add(substring[left:right + 1])
                left -= 1
                right += 1
            else:
                break
    for i in range(len(substring)):
        expand_around_center(i, i)
        if i + 1 < len(substring):
            expand_around_center(i, i + 1)
    filtered_palindromes = {p for p in matched_palindromes if 13 <= len(p) <= 66}
    return filtered_palindromes