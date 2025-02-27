def palindromes_between_indices(s):
    substring = s[2:10].lower()
    length = len(substring)
    if length < 7:
        return set()
    characters = list(substring)
    palindromes = set()

    def permute(data, m=[]):
        if len(m) == 7:
            candidate = ''.join(m)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
        else:
            for i in range(len(data)):
                permute(data[:i] + data[i + 1:], m + [data[i]])
    permute(characters)
    return palindromes