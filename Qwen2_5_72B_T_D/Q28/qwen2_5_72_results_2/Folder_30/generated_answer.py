def return_nth_smallest_ascii(s):
    relevant_chars = s[50:77]
    relevant_asciis = [ord(ch) for ch in relevant_chars]
    relevant_asciis.sort()
    return chr(relevant_asciis[10]) if len(relevant_asciis) > 10 else None