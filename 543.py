# Get the diameter of the binary tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def getDiameterUtil(root,ans):
    if root is None:
        return 0
    left=getDiameterUtil(root.left,ans)
    right=getDiameterUtil(root.right,ans)
    # print(root.data,left,right)
    if (left+right)>ans[0]:
        ans[0]=left+right
    return max(left,right)+1

def getDiameter(root):
    ans=[0]
    getDiameterUtil(root,ans)
    return ans[0]

if __name__ == '__main__':

    # root=Node(1)
    # root.left=Node(2)
    # root.right=Node(3)
    # root.left.left=Node(4)
    # root.left.right=Node(5)
    root=Node(1)
    root.left=Node(2)
    root.left.left=Node(3)
    root.left.right=Node(5)
    root.left.left.left=Node(4)
    root.left.right.right=Node(6)
    print(getDiameter(root))
