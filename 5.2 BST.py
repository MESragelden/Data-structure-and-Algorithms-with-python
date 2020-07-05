class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)
    def getIndex(self,Node,new_val):
        if Node.value < new_val:
            if Node.right == None:
                return Node
            else :
                return self.getIndex(Node.right,new_val)
        else : 
            if Node.left == None:
                return Node
            else :
                return self.getIndex(Node.left,new_val) 
            

    def insert(self, new_val):
        n = self.getIndex(self.root,new_val)
        if n.value > new_val:
            n.left = Node(new_val)
        else :
            n.right = Node(new_val) 

    def goSearch(self,Node,find_val):
        if Node:
            if find_val == Node.value:
                return True
            elif find_val > Node.value:
                self.goSearch(Node.right,find_val)
            else :
                self.goSearch(Node.left,find_val)
        else :
            return
        return False

    def search(self, find_val):
        return self.goSearch(self.root,find_val)     
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))