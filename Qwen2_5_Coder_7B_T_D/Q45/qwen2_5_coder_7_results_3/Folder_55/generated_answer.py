def palindromes_between_indices(s):
    result = set()
    for i in range(len(s) - 2):
        substring = s[i:i + 3]
        if substring.lower() == substring[::-1].lower():
            result.add(substring)
    return result