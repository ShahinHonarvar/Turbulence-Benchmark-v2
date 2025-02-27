def palindromes_of_specific_lengths(s):
    length_range = range(136, 161)
    result_set = set()
    for i in length_range:
        start = 100
        while start + i - 1 <= 295:
            substring = s[start:start + i].lower()
            if substring.isalpha() and substring == substring[::-1]:
                result_set.add(substring)
            start += 1
    return result_set