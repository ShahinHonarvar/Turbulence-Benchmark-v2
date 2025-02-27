def palindromes_between_indices(s):
    subset = s[4:9]
    subset = ''.join(filter(str.isalpha, subset)).lower()
    chars = list(subset)
    chars.sort()
    result = set()

    def permute(data, m=[]):
        if len(m) == 3:
            candidate = ''.join(m)
            if candidate == candidate[::-1]:
                result.add(candidate)
            return
        for i in range(len(data)):
            permute(data[:i] + data[i + 1:], m + [data[i]])
    permute(chars)
    return result