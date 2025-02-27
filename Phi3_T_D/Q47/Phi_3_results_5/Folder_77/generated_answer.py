def palindromes_of_specific_lengths(s):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
            if left > 103 or right < 276:
                break
            if left == right or s[left].lower() == s[right].lower():
                if right - left + 1 >= 100 and right - left + 1 <= 169:
                    palindromes.add(s[left:right + 1])
                left -= 1
                right += 1
            else:
                break
    palindromes = set()
    s = s[103:277]
    for i in range(len(s)):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)
    return palindromes