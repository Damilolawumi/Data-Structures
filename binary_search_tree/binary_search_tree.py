from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # left case
        if value < self.value:  # check if our newnodes value is less than the current node value
            if self.left is None: # does it have a child to the left?
                self.left = BinarySearchTree(value)  # place new node here
                return
            else:
            # repeat process for the left
                self.left.insert(value)

        # Right case
        if value >= self.value:  # check if the new node is >= the crrent node value
            if self.right is None: #if no child
                self.right = BinarySearchTree(value) #place new node here 
                return
            else:
            # repeat process for the right
                self.right.insert(value)

        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if self.value == target: #check if target is equal to value
            return True

        if target < self.value: #check if target is less than value
            if self.left is None: #check to see if ther isnt any child node to the left
                return False  
            else:
                left_node = self.left
                # call the contains method of the left child
                return left_node.contains(target)     

        if target >= self.value:
            if self.right is None:
                return False
            else:
                right_node = self.right
                # call the contains method of the right child
                return right_node.contains(target)             

      

    # Return the maximum value found in the tree

    def get_max(self):
        # check the base case to see if theres a value
        if self.value is None:
            return None
        #if there is no right value
        if self.right is None:
            return self.value #return the root value
        else:
            # return the get max of the right hand child
            return self.right.get_max()    
        
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
                       
            cb(self.value)# run the cb and pass the self value
           
            if self.left != None: # if the left of the current node is not None
                
                self.left.for_each(cb)# run the for each method on left
           
            if self.right != None: # if the right of the current node is not None
                
                self.right.for_each(cb) # run the for each method on right

        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
