import ast

def generate__code(text_specification):
    spec_tree = ast.parse(text_specification)
    func_node = spec_tree.body[0]
    func_name = func_node.name
    func_args = func_node.args.args
    func_body = func_node.body
    func_code = ast.unparse(func_node)
    return func_code