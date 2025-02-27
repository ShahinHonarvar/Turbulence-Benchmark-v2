def palindrome_of_length_at_least_n(text):
    text_lower = text.lower()
    palindromes = set()
    str_len = len(text)

    def expand_around_center(left, right):
        while left >= 0 and right < str_len and (text_lower[left] == text_lower[right]):
            left -= 1
            right += 1
        return text_lower[left + 1:right]
    for i in range(str_len):
        palindromes.add(expand_around_center(i, i))
        if i + 1 < str_len:
            palindromes.add(expand_around_center(i, i + 1))
    return {p for p in palindromes if len(p) >= 22}