def palindromes_of_specific_lengths(s):

    def is_english_letter(c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and is_english_letter(s[left]) and is_english_letter(s[right]):
            if s[left].lower() == s[right].lower():
                yield s[left:right + 1]
            else:
                break
            left -= 1
            right += 1
    palindromes = set()
    for i in range(21, 62):
        for length in range(22, 34):
            if i - length // 2 >= 0 and i + length // 2 < len(s):
                for palindrome in expand_around_center(i - length // 2, i + length // 2):
                    palindromes.add(palindrome)
    return palindromes