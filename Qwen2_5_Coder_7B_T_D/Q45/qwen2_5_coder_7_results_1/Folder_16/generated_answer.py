def palindromes_between_indices(s):
    letters = [char.lower() for char in s[6:10] if char.isalpha()]
    if len(letters) < 5:
        return set()
    letters.sort()
    result = set()
    for i in range(len(letters)):
        for j in range(i + 5, len(letters) + 1):
            sub = ''.join(letters[i:j])
            if sub == sub[::-1]:
                result.add(sub)
    return result