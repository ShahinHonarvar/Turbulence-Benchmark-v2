def palindromes_of_specific_lengths(s):
    result = set()
    start = 10
    end = min(len(s), 55)
    for l in range(3, 8):
        for i in range(start, end - l + 1):
            substring = s[i:i + l].lower()
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result