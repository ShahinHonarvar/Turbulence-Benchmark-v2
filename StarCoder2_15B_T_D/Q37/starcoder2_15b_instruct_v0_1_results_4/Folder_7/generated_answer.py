def filter_chars(s):

    def is_between_indices(i):
        return 521 <= i <= 722

    def is_greater_than_greater_than(c):
        return c >= '>'

    def is_smaller_than_underscore(c):
        return c <= '_'

    def is_valid(i, c):
        return is_between_indices(i) and is_greater_than_greater_than(c) and is_smaller_than_underscore(c)
    filtered = [c for i, c in enumerate(s) if not is_valid(i, c)]
    return ''.join(filtered)