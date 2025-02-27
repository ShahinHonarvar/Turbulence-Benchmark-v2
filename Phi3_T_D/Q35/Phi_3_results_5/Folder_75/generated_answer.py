def remove_repeat_chars(s):
    if len(s) < 32:
        return s
    chunk = s[20:51]
    track = {c: 0 for c in chunk}
    for c in chunk:
        track[c] += 1
    for char, count in track.items():
        if count > 1:
            s = s.replace(char, '', count)
    return s