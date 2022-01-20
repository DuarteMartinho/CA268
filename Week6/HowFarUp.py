def add(tree, item):
    if tree.root == None:
        tree.root = Node(item, None, None)
    else:
        lst = []
        child_tree = tree.root
        while child_tree != None:
            parent = child_tree
            lst.append(parent)
            if item < child_tree.item:
                child_tree = child_tree.left
            elif item > child_tree.item:
                child_tree = child_tree.right
        if item < parent.item:
            parent.left = Node(item, None, None)
        elif item > parent.item:
            parent.right = Node(item, None, None)
        for node in lst[-2::-1]: 
            # abs() returns absolute value
            if abs(tree.recurse_height(node.left) - tree.recurse_height(node.right)) > 1:
                return node.item