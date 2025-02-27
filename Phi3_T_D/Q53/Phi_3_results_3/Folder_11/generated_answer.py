from collections import defaultdict

def palindrome_of_length_at_least_n(s):

    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha() and (s[left].lower() == s[right].lower()):
            yield s[left:right + 1]
            left -= 1
            right += 1

    def find_palindromes(s):
        palindromes = set()
        for i in range(len(s)):
            odd_pal = [p for p in expand_around_center(s, i, i)]
            even_pal = [p for p in expand_around_center(s, i, i + 1) if len(p) >= 54]
            palindromes.update(odd_pal)
            palindromes.update(even_pal)
        return palindromes
    return find_palindromes(s)