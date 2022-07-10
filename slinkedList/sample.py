import slinkedList as ll

# main method

# creating LinkedList
m= ll.SingleLinkedList(data=[1,2,3,4])
n= ll.SingleLinkedList(data=[5,6,7])
o=m+n
print(o)
# for x in o:
#     print(x.data)
# print(m.equal(n))
# print(m+n)
# print(n.length())
# a=m.headNode()
# print(a.getNextNode().getData())
# n= ll.Single_LinkedList([1,2,1,2,1,2,3])
# # t=m.slice(start=2,end=8,step=2)
# b=n.datanode(2)
# # m.insertPos({4:44,5:55})
# # m.addToEnd("hi")
# # m.addToEnd([1,2,3,4])
# # m.addToEnd({6,7,8})
# # m.addToEnd((9,10))
# #m.insertPos({4:44,1:"hii",3:"oyy",2:222})
# # m.insertAfter(a,(6,7,8))
# # n=m.new_sorted(reverse=True)
# #print(n.toList())
# # m.remove_duplicates()
# # print(m.doesHaveType([int,float,str]))
# m.insertAfter(ref_node=a,nodes=[a.getNextNode(),a])
# print(o.toList())



# # adding some elements to the End of the LinkedList
# myList.addToEnd(12)
# myList.addToEnd(13)
# myList.addToEnd(3)

# # printing Length
# print(myList.length())

# # printing index of an element
# print(myList.index(3))

# # printing element at a particular index
# print(myList.atIndex(5))

# # removing an element
# print(myList.removeItem(12))

# # removing element from a particular position
# myList.removeAtPosition(2)


# # printing max and min element
# print(myList.Max())
# print(myList.Min())

# # pushing and poping elements
# print(myList.push(31))

# print(myList.pop())


# # creating a copy of the Linked List
# myList2 = myList.copy()

# # removing all elements from the LinkedList
# myList2.clear()


# # printing a string of elements of the LinkedList
# print(myList.toString(","))

# # printing count of particular element in the List
# print(myList.count(3))

# # making a builtIn List from the LinkedList
# newList = myList.toList()
# print(newList)

# # making a List from the LinkedList
# newSet = myList.toSet()
# print(newSet)

# # reversing the LinkedLkst
# myList.reverse()

# # making a sorted LinkedList out of the Original
# myList3 = myList.new_sorted()

# # sorting the LinkedList
# myList.sorted()