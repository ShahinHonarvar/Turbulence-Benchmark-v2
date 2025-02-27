def palindromes_between_indices(s):
    letters = s[2:9].lower()
    unique_letters = set(letters)
    if len(unique_letters) < 7:
        return set()
    result = set()
    for i in range(len(letters)):
        for j in range(i + 7, len(letters) + 1):
            if letters[i:j] == letters[i:j][::-1]:
                result.add(letters[i:j])
    return result