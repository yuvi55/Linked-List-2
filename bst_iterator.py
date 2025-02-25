# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    stack = []
    def __init__(self, root: Optional[TreeNode]):
        self.dfs(root)

    def next(self) -> int:
        node = self.stack.pop(0)

        if node.right != None:
            self.dfs(node.right)
        
        return node.val

    def hasNext(self) -> bool:
        if len(self.stack) > 0:
            return True
        else:
            return False

    def dfs(self,root):
        while root != None:
            self.stack.insert(0,root)
            root = root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
