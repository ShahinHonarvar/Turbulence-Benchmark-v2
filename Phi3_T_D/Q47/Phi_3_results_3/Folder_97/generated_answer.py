def palindromes_of_specific_lengths(s):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
            if left >= 28 and right <= 94 and (left + right + 1 - 1 <= 49):
                yield s[left:right + 1].lower()
            left -= 1
            right += 1
    palindromes = set()
    for i in range(28, 95):
        for j in [i, i + 1]:
            for palindrome in expand_around_center(i, j):
                if len(palindrome) >= 38 and len(palindrome) <= 49:
                    palindromes.add(palindrome)
    return palindromes