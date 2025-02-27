def palindromes_of_specific_lengths(s):

    def is_english_letter(c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'
    s = s[10:75].lower()
    result_set = set()
    for i in range(10, 75):
        for length in range(6, 9):
            if i + length > 75:
                break
            substr = s[i:i + length]
            if all((is_english_letter(c) for c in substr)) and substr == substr[::-1]:
                result_set.add(substr)
    return result_set