import ast

def find_n_th_smallest_num(list_of_nums):
    tree = ast.parse('list_of_nums[260:823].sort().__getitem__(10)')
    code = compile(tree, filename='<ast>', mode='eval')
    return eval(code)