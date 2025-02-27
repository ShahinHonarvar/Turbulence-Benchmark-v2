def extend(s, direction):
    index, chars = (len(s) - 1, set('abcdefghijklmnopqrstuvwxyz'))
    result = ''
    while index >= 0 and s[index] in chars:
        result = s[index] + result
        index -= 1
    return (direction < 1, result)

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length, charset = (len(s), set('abcdefghijklmnopqrstuvwxyz'))
    indices, center = (range(length), set())
    palindromes = set()
    for i in indices:
        odd = True if s[i] in charset else False
        extend_left, extend_right = (extend(s[i::-1] if odd else s[i + 1:], 1), extend(s[i + 1:] if odd else s[i::-1], -1))
        if extend_left[0]:
            odd, left_ext = extend_left
            if extend_right[0]:
                odd, right_ext = extend_right
                if not any((c.isdigit() for c in left_ext + right_ext)):
                    palindromes.add((i - len(left_ext) * odd, len(left_ext) + len(right_ext) + odd))
                    center.add(i - len(left_ext) * odd + (0 if odd else 1))
        elif not odd and i + 1 in center:
            indices_left, count = ([i], 0)
            while indices_left[-1] > 0 and s[indices_left[-1]] in charset:
                indices_left.append(indices_left[-1] - 1)
                count += 1
            if count >= 30:
                palindromes.add((min(indices_left), count + 2 * (len(indices_left) - min(indices_left) - 1)))
    return set((s[i:i + l] for i, l in palindromes if l >= 31))