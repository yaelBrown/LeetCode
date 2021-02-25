# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _dfs(r, cnt):
            if r == None: 
              return cnt
            if r.left == None and r.right == None: 
                return cnt
            c = d = 0
            if r.left != None: 
                c = _dfs(r.left, cnt + 1)
            if r.right != None: 
                d = _dfs(r.right, cnt + 1)

            return max(c,d)
        if root == None:
            return 0
        else: 
            return _dfs(root, 1)
			

