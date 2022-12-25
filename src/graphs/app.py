class TreeGenerator():
    def __init__(self):
        self.parents = []
        self.children = []

    def get_roots(self, source: list[tuple]) -> dict:
        # roots = []
        roots = {}
        for item in source:
            parent, child = item
            if parent is None:
                roots[child] = {}
            else:
                self.parents.append(parent)
                self.children.append(child)
        return roots

    def to_tree(self, source: list[tuple]) -> dict:
        root = self.get_roots(source)
        myroot = {}
        for i in root:
            myroot[i] = self.return_my_children(i)
        return myroot

    def return_my_children(self, parent: str) -> dict:
        child = {}
        while True:
            try:
                ind = self.parents.index(parent)
                self.parents.pop(ind)
                ch = self.children.pop(ind)
                child[ch] = self.return_my_children(ch)
            except ValueError:
                return child


def to_tree(source):
    tree_generator = TreeGenerator()
    return tree_generator.to_tree(source)
