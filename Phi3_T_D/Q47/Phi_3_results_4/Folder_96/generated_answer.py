from itertools import product

def palindromes_of_specific_lengths(text):
    start, end = (100, 300)
    shortest, longest = (50, 100)
    s = text[start:end].lower()
    palindromes = set()

    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
            if left == right:
                center = s[left]
                while left >= 0 and right < len(s) and (s[left] == center) and (len(s[left:right + 1]) <= longest):
                    palindromes.add(s[left:right + 1])
                    left -= 1
                    right += 1
                left += 1
                right -= 1
            elif s[left] == s[right]:
                palindromes.add(s[left:right + 1])
                left -= 1
                right += 1
            else:
                break
    for i in range(start, end):
        expand_around_center(s, i, i)
        if i + 1 < len(s) and s[i] == s[i + 1]:
            expand_around_center(s, i, i + 1)
    valid_palindromes = {p for p in palindromes if shortest <= len(p) <= longest and p.isalpha()}
    return valid_palindromes