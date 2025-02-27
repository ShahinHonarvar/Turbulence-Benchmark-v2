def all_substring_of_size_n(s):

    def is_unique(substring):
        return len(substring) == len(set(substring))
    return [s[i:i + 130] for i in range(len(s) - 129) if is_unique(s[i:i + 130])]