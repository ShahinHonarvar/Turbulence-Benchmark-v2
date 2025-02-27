def palindromes_of_specific_lengths(s):
    length = len(s)
    result_set = set()
    for start in range(200, 301):
        for end in range(start, start + 10):
            if end > length - 1 or end - start < 10 or end - start > 50:
                continue
            substring = s[start:end]
            if all((char.isalpha() and chr(ord('a')).lower() <= char.lower() <= chr(ord('z')).lower() for char in substring)):
                if substring.lower() == substring[::-1].lower():
                    result_set.add(substring)
    return result_set