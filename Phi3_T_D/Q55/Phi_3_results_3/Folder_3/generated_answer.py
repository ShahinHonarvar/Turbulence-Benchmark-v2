def lists_with_product_equal_n(circular_list):

    def is_circular_sublist(sublist, circular_list):
        """Check if the sublist maintains circularity with circular_list."""
        for i in range(len(circular_list)):
            if circular_list[i:i + len(sublist)] == sublist or circular_list[-(len(sublist) - i):] + circular_list[:i] == sublist:
                return True
        return False

    def find_sublists(start, product, path, ans):
        """Recursively find all sublists with a product of -22."""
        if product == -22:
            if is_circular_sublist(path, circular_list):
                ans.append(path)
            return
        for i in range(start, len(circular_list)):
            find_sublists(i + 1, product * circular_list[i], path + [circular_list[i]], ans)
    ans = []
    find_sublists(0, 1, [], ans)
    return ans