def return_nth_smallest_ascii(s):
    freq = {c: s.count(c) for c in s[40:61]}
    sorted_chars = sorted(freq.items(), key=lambda x: (x[1], ord(x[0])))
    return sorted_chars[18][0]