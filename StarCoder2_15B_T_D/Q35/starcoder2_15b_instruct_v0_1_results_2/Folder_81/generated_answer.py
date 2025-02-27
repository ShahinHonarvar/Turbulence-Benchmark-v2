def remove_repeat_chars(text):
    counts = {}
    for ch in text[20:200]:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in counts:
        if counts[ch] > 1:
            text = text.replace(ch, '')
    return text