def palindromes_of_specific_lengths(s):
    s = s[127:289].lower()
    result = set()
    for start in range(len(s) - 118):
        for length in range(119, 142):
            if start + length > len(s):
                break
            sub = s[start:start + length]
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result