def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        if r - l + 1 >= 112:
            yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text)):
        for pal in expand_around_center(text, i, i):
            palindromes.add(pal)
        for pal in expand_around_center(text, i, i + 1):
            palindromes.add(pal)
    return palindromes