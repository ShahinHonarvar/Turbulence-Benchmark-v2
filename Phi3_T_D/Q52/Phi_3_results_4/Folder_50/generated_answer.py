from collections import defaultdict

def palindrome_of_length_n(s):

    def expand(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            yield (left, right)
            left -= 1
            right += 1
    palindromes = set()
    length = len(s)
    odd_count, even_count = (defaultdict(int), defaultdict(int))
    for i in range(length):
        c = s[i].lower()
        odd_count[i, c] += 1
    for i in range(length + 1):
        if i > 0 and s[i - 1].lower() == s[i - 2].lower():
            even_count[i, s[i - 1].lower()] = odd_count[i - 1, s[i - 1].lower()] + 1
        else:
            even_count[i, s[i - 1].lower()] = odd_count[i - 1, s[i - 1].lower()]
    for i in range(length + 1):
        for j in range(i, length):
            odd_center = (i - 1) // 2
            even_center = (j - 1) // 2
            if even_center > odd_center:
                if (j + 1) % 2 == 0:
                    c_len = (j - i) // 2
                    if c_len == 20 and even_count[i, s[i - 1].lower()] >= c_len:
                        palindromes.add(s[i:j + 1].lower())
                elif odd_count[(i + j) // 2, s[(i + j) // 2].lower()] >= (j - i) // 2:
                    palindromes.add(s[i:j + 1].lower())
            elif (j + 1) % 2 == 0:
                c_len = (j - i) // 2
                if c_len == 20 and even_count[i, s[i - 1].lower()] >= c_len:
                    palindromes.add(s[i:j + 1].lower())
            elif odd_count[i, s[i].lower()] >= (j - i) // 2:
                palindromes.add(s[i:j + 1].lower())
    return {p[:40] for p in palindromes}