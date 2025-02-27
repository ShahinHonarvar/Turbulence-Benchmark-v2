def palindromes_of_specific_lengths(s):
    start_idx = 127
    end_idx = 288

    def is_valid_char(c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

    def expand(left, right):
        while left >= start_idx and right <= end_idx:
            if not (is_valid_char(s[left]) or is_valid_char(s[right])):
                break
            if s[left].lower() != s[right].lower():
                break
            yield (-right, -left)
            left -= 1
            right += 1
    palindromes = set()
    for length in range(119, 142):
        for i in range(start_idx, end_idx - length + 1):
            for pal in expand(i, i + length - 1):
                palindromes.add(s[pal[0] + 1:-pal[1]])
    return palindromes