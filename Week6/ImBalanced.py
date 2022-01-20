def recursive_rotation_type(bst, ptr):
    if ptr.left != None:
        return recursive_rotation_type(bst, ptr.left) + "l"
    elif ptr.right != None:
        return recursive_rotation_type(bst, ptr.right) + "r"
    else:
        return ""
def rotation_type(bst):
    return recursive_rotation_type(bst, bst.root)