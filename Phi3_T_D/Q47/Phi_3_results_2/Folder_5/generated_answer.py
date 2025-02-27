def palindromes_of_specific_lengths(s):
    index_range = (63, 70)
    result = {s[i:j + 1].lower() for i in range(index_range[0], index_range[1] + 1) for j in range(i, index_range[1] + 1) if 3 <= j - i <= 4 and s[i:j + 1].isalpha() and (s[i:j + 1].lower() == s[i:j + 1].lower()[::-1])}
    return result