#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
def max_height(root):
    if root is None:
        return -1
    else:
        #print(root.data)
        ldepth = max_height(root.left)
        rdepth = max_height(root.right)

        if ldepth > rdepth:
            return ldepth+1
        else:
            return rdepth +1
class Solution:
    #Function to find the height of a binary tree.
    #@staticmethod


    def height(self, root):
        # code here

        return(max_height(root))