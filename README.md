# slinkedList


## What is it?

**slinkedList** is a module to automate the operations that can be performed using linked list such as creating a new node, adding a new element,inserting an element at the head node, tail node and required location, merging the linked lists,sorting,duplicates removing and deleting the elements etc.


## Where to get it

The source code is currently hosted on GitHub at: [here](https://github.com/Sree-Ramya-Gudiwada/slinkedList)

 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install slinkedList.



## Features 

slinkedList can apply the following operations:
* creating a single liked list with data
* adding a node at starting,ending and particular position of the linked list 
* removing node at starting,ending and particular position of the linked list
* Basic statistics like sum, min, max, mean, mode and median
* converting the linked list data to string, list, tuple and set
* counting the data occurrences in given linked list  
* sorting the linked list and assign the values in sorted way
* Searching particular data items in liked list
* Replacing the values with new data
* Slicing the linked list
* Removing duplicates, equalizing two liked lists, merging two linked list, copy, clear, push, pop, isempty, lenght etc etc..
* The main advantage of this linked list is we can traverse using for loop and this linked list has operator overloading so we can perform +, -, *, **, /, //,%, [], +=,-= etc etc operations

## Installation

slinkedList requires [Python 3](https://www.python.org/downloads/) . 

To install using pip, use

`pip install slinkedList`

## Usage

* **Import the library**:


``` python
import slinkedList as ll
```

* **creating a empty linked list**

 
``` python
empty_list= ll.SingleLinkedList() 
```
 
* **creating linked list with data**

``` python
temp = ll.SingleLinkedList([1,2,3,4])
```
 
* **Some most commonly used operations**
 
 
``` python
myList=ll.SingleLinkedList([1,2,3,4,5,6,7,8]) #creating ll with data
myList.addToEnd(12) #adds 12 to the ending

# printing Length
print(myList.length())

# printing indexes of given elements
print(myList.index([2,3,4]))

# printing elements at a particular indexes
print(myList.atIndex([3,1]))

# removing an element
print(myList.removeItem([12,1]))

# removing elements from a particular positions
myList.removeAtPosition([3,2,4])

#returns a list with descending order
new_list=myList.new_sorted(reverse=True)

```

## Examples
**1)**
``` python
import slinkedList as ll

# creating LinkedList
m= ll.SingleLinkedList(data=[1,2,3,4])
n= ll.SingleLinkedList(data=[5,6,7])
o=m+n
print(o)
```

**returns,**

``` Python
sllist([1, 2, 3, 4, 5, 6, 7])
```
----
**2)**
``` Python
import slinkedList as ll
m= ll.SingleLinkedList(data=[1,2,3,4,5,6,7,8])
print(m[:4].toString("->"))
```

returns,

``` Python
1->2->3->4
```
----
**3)**
``` Python
import slinkedList as ll
m= ll.SingleLinkedList(data=[1,2,3,4])
print(reversed(m))
```

returns,

``` Python
sllist([4, 3, 2, 1])
```

----

## Documentation

The official documentation is hosted on Drive : [doc](https://docs.google.com/document/d/1GfWs0_5z17KHiGMBuHMYKNjl566AtlcB/edit?usp=sharing&ouid=116424253329736412646&rtpof=true&sd=true)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License

##### MIT

For any questions, issues, bugs, and suggestions please visit [here](https://github.com/Sree-Ramya-Gudiwada/slinkedList/issues)

