def return_nth_smallest_ascii(string):
    relevant_chars = string[62:84]
    return sorted(relevant_chars, key=ord)[8]