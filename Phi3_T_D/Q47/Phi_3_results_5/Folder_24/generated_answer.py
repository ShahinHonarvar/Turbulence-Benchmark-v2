def palindromes_of_specific_lengths(s):
    match = s[12:93]
    results = set()
    for end in range(42, 78):
        for start in range(13, 93 - end + 1):
            sub = match[start:start + end]
            if sub == sub[::-1] and all((char.isalpha() for char in sub)) and ('a' <= sub.lower() <= 'z'):
                results.add(sub.lower())
    return results