def palindromes_between_indices(s):
    result = set()
    substring = s[1:9].lower()
    letters = list(substring)
    for i in range(len(letters)):
        for j in range(i + 6, len(letters) + 1):
            candidate = ''.join(letters[i:j])
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result