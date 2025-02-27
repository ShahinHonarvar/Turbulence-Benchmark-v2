def return_nth_smallest_ascii(s):
    window = s[33:61]
    ascii_values = sorted(set((ord(c) for c in window)))
    return chr(min((a for a in ascii_values if window.count(chr(a)) >= 18)))