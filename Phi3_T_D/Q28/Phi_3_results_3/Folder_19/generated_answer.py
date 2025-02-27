def return_nth_smallest_ascii(s):
    relevant_chars = [ord(c) for c in s[0:19]]
    relevant_chars.sort()
    return chr(sorted(set(relevant_chars))[12])