def return_nth_smallest_ascii(s):
    filtered = [char for char in s[:13] if s.count(char) == 1]
    return min(filtered, key=lambda c: ord(c)) if filtered else None