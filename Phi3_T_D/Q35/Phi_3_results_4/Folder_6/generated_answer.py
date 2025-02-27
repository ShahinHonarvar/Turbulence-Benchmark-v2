def remove_repeat_chars(s):
    start, end = (20 + 1, 93 + 1)
    counts = {}
    for i in range(start, end):
        ch = s[i]
        counts[ch] = counts.get(ch, 0) + 1
    altered = []
    for i in range(len(s)):
        ch = s[i]
        if i >= start and i < end and (counts[ch] > 1) or (i < start or i >= end):
            altered.append(ch)
    return ''.join(altered)