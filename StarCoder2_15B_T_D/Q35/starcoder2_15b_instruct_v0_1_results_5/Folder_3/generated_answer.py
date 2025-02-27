def remove_repeat_chars(s: str) -> str:
    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    output = []
    for i, c in enumerate(s):
        if freq[c] > 1 and 56 <= i < 88:
            continue
        output.append(c)
    return ''.join(output)