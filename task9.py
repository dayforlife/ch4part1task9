# my_list = [5, 20, 78, 93, 10, 27, 4, 43, 67, 18, 81, 98, 36]
# my_list.sort()
# print(my_list)

# def binarysearch(my_list, find, start, stop):
#     if start > stop:
#         return False
#     else:
#         mid = (start+stop) //2
#         if find == my_list[mid]:
#             return mid
#         elif find < my_list[mid]:
#             return binarysearch(my_list,find, start, mid - 1)
#         else:
#             return binarysearch(my_list, find, mid + 1, stop)


# find = 13
# start = 0
# stop = len(my_list)
# x = binarysearch(my_list, find, start, stop)

# if x == False:
#     print("Item", find, "Not found")
# else:
#     print("Item", find, "Found at index", x)

# class Node():
#     def __init__(self, value=None):
#         self.value = value
#         self.left_child=None
#         self.right_child=None

# class Binarysearch():
#     def __init__(self):
#         self.root=None
    
#     def insert(self, value):
#         if self.root == None:
#             self.root=Node(value)
#         else:
#             self._insert(value, self.root)

#     def _insert(self, value, cur_node):
#         if value<cur_node.value:
#             if cur_node.left_child==None:
#                 cur_node.left_child=Node(value)
#             else:
#                 self._insert(value, cur_node.left_child)
#         elif value>cur_node.value:
#             if cur_node.right_child==None:
#                 cur_node.right_child=Node(value)
#             else:
#                 self._insert(value, cur_node.right_child)
#         else:
#             print("Value already in Tree")
    
#     def print_tree(self):
#         if self.root!=None:
#             self._print_tree(self.root)
    
#     def _print_tree(self, cur_node):
#         if cur_node!=None:
#             self._print_tree(cur_node.left_child)
#             print(str(cur_node.value))
#             self._print_tree(cur_node.right_child)
    
#     def height(self):
#         if self.root!=None:
#             return self._height(self.root, 0)
#         else:
#             return 0
    
#     def _height(self, cur_node, cur_height):
#         if cur_node==None: return cur_height
#         left_height=self._height(cur_node.left_child, cur_height+1)
#         right_height=self._height(cur_node.right_child, cur_height+1)
#         return max(left_height, right_height)

#     def search(self, value):
#         if self.root!=None:
#             return self._search(value, self.root)
#         else:
#             return False

#     def _search(self, value, cur_node):
#         if value == cur_node.value:
#             return True
#         elif value<cur_node.value and cur_node.left_child!=None:
#             return self._search(value, cur_node.left_child)
#         elif value>cur_node.value and cur_node.right_child!=None:
#             return self._search(value, cur_node.right_child)
#         return False



# def fill_tree(tree, num_elems=100, max_int=1000):
#     from random import randint
#     for _ in range(num_elems):
#         cur_elem = randint(0, max_int)
#         tree.insert(cur_elem)
#     return tree


# tree = Binarysearch()
# tree.insert(4)
# tree.insert(7)
# tree.insert(2)
# tree.insert(1)
# tree.insert(12)
# tree.insert(3)
# tree.insert(5)

# tree.print_tree()

# print("tree height: " + str(tree.height()))
# print(tree.search(500))
# print(tree.search(30))

def lca(root, v1, v2):
# compare v1 v2 and get the big and small value
    if v1 > v2:
        v_big, v_small = v1, v2
    else:
        v_big, v_small = v2, v1

    current = root
    while True:
        if current.info > v_big:
            current = current.left
        elif current.info < v_small:
            current = current.right
        elif current.info >= v_small and current.info <= v_big:
            return current

lca()