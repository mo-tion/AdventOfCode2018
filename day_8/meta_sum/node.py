class Node:
    def __init__(self, num_meta, num_children):
        self.num_meta = num_meta
        self.num_children = num_children
        self.children = []
        self.metas = []

    def add_child(self, child_node):
        if len(self.children) >= self.num_children:
            raise 
        else:
            self.children.append(child_node)

    def add_meta(self, meta):
        if len(self.metas) >= self.num_meta:
            raise 
        else:
            self.metas.append(meta)

    def missing_children(self):
        return num_children - len(self.child_node)

    def missing_meta(self):
        return num_meta - len(self.metas)

    def sum_meta(self):
        child_sum = 0
        for child in self.children:
            child_sum += child.sum_meta()
        meta_sum = reduce(lambda x,y: x+y, self.metas)
        return child_sum + meta_sum