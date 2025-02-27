def generate_permutations(chars, depth, path, length):
    if depth == length:
        if path == path[::-1]:
            result.add(path)
        return
    for i in range(len(chars)):
        generate_permutations(chars[:i] + chars[i + 1:], depth + 1, path + chars[i], length)

def palindromes_between_indices(s):
    english_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    chars = ''.join([c.lower() for c in s[4:10] if c in english_chars])
    result = set()
    for length in range(6, len(chars) + 1):
        generate_permutations(chars, 0, '', length)
    return result