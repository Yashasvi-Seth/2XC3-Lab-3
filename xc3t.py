class XCThreeTree:
    def __init__(self, degree):
        self.degree = degree
        self.children = []

        for i in range(1, degree + 1):  # 1-based child numbering
            child_degree = i - 2 if i > 2 else 0
            self.children.append(XCThreeTree(child_degree))

    def nodes(self):
        return 1 + sum(child.nodes() for child in self.children)

    def height(self):
        if not self.children:
            return 0
        return 1 + max(child.height() for child in self.children)