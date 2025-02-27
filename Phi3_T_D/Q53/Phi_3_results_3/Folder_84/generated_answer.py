def find_palindromes(s, length):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            if right - left + 1 >= length:
                return set(s[left:right + 1])
            left -= 1
            right += 1
        return set()
    all_palindromes = set()
    for i in range(len(s)):
        odd_palindromes = expand_around_center(i, i)
        even_palindromes = expand_around_center(i, i + 1)
        all_palindromes.update(odd_palindromes, even_palindromes)
    return {pal for pal in all_palindromes if len(pal) >= length}

def palindrome_of_length_at_least_n(s):
    return find_palindromes(s, 81)