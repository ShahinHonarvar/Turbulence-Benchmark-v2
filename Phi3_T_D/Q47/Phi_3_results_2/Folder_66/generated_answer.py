def palindromes_of_specific_lengths(s: str) -> set:

    def expand(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()) and s[left].isalpha():
            if 32 <= left <= 79 and 32 <= right <= 79:
                palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
    palindromes = set()
    for i in range(32, 79):
        if s[i].isalpha():
            expand(i, i)
            if i + 1 <= 79 and s[i + 1].isalpha():
                expand(i, i + 1)
    return {p.lower() for p in palindromes if 35 <= len(p) <= 41}