def tree_by_levels(node):
    def traverse(node, res={}, level=1):
        if node is not None:
            try:
                res[level] += [node.value]
            except KeyError:
                res[level] = [node.value]
            traverse(node.left, res, level+1)
            traverse(node.right, res, level+1)
        return res
    level_dict = dict(sorted(traverse(node).items()))
    res = sum(level_dict.values(), [])
    return res
