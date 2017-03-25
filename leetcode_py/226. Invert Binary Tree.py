# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        while stack:
            t= stack.pop()
            if t:
                t.left,t.right = t.right,t.left
                stack.append(t.left)
                stack.append(t.right)
        return root

class Solution2(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left,root.right = root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

if __name__ == '__main__':
    root  = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    root.left=a
    root.right=b
    Solution().invertTree(root)
    print root.left.val,root.right.val