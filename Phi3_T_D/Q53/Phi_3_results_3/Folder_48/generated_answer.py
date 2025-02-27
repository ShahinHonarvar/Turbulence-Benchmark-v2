def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and (s[left] == s[right] or (left >= 1 and right < len(s) - 1 and (s[left - 1:right + 1] in set([s])))):
        yield s[left:right + 1]
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        pals = list(expand_around_center(string, i, i)) + list(expand_around_center(string, i, i + 1))
        for pal in pals:
            if len(pal) >= 150:
                palindromes.add(pal)
    return palindromes