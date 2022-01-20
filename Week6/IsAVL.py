def is_avl(bst):
    ptr = bst.root
    bst.root = bst.root.left
    height = bst.height()
    bst.root = ptr
    bst.root = bst.root.right
    height2 = bst.height()
    
    return not (height > height2 + 1 or height2 > height + 1)