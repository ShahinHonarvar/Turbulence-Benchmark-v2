def expand_around_center(s, left, right):
    pairs = set()
    while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha():
        if s[left].lower() == s[right].lower():
            pairs.add(s[left:right + 1])
            left -= 1
            right += 1
        else:
            break
    return pairs

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        odd_pairs = expand_around_center(s, i, i)
        for pair in odd_pairs:
            if len(pair) >= 99:
                result.add(pair)
        even_pairs = expand_around_center(s, i, i + 1)
        for pair in even_pairs:
            if len(pair) >= 99:
                result.add(pair)
    return result