from exceptions import incorrect_type
import acc_types as tt
import math
# program to implement Linked List

class SingleLinkedList:
    def __init__(self,data=None,node=None):
        self.head = None
        try:
            if data==None and (type(node)==Node or type(node) in tt.mtype):
                self.addToEnd(node=node)
            elif data!=None and (type(data) in tt.stype or type(data) in tt.mtype):
                self.addToEnd(data=data)
            elif data==None and node==None:
                return None
            else:
                raise TypeError("Incorrect type given")
        except:
            raise TypeError("Incorrect type given")
            
    #operator overloading
    def __add__(self, o):
        if o.head==None:
            return self
        else:
             try:   
                temp=self.copy()
                temp.merge(o)
                return temp
             except:
                raise TypeError("Incorrect type given")
                
            
    def __iadd__(self, o):
        if o.head==None:
            return self
        else:
             try:   
                self.merge(o)
                return self
             except:
                raise TypeError("Incorrect type given")
    
    def __sub__(self, o):
        if self.length()!=o.length():
            raise incorrect_type("Incorrect type given")
        if self.head==None:
            raise incorrect_type("Incorrect type given")
        temp=SingleLinkedList()
        for start,start2 in zip(self,o):
            try:
                temp.addToEnd(data=start.getData()-start2.getData())
            
            except:
                raise incorrect_type("Incorrect type given")
        return temp
    
    def __mul__(self, o):
        if type(o)==int:
            temp=self.copy()
            for i in range(o-1):
                temp.merge(self.copy())
            return temp
        elif type(o) in tt.stype  or type(o) in tt.mtype:
                raise incorrect_type("Incorrect type given")
        else:
            if self.length()!=o.length():
                raise incorrect_type("Incorrect type given")
            if self.head==None:
                raise incorrect_type("Incorrect type given")
            temp=SingleLinkedList()
            for start,start2 in zip(self,o):
                try:
                    temp.addToEnd(data=start.getData()*start2.getData())
                
                except:
                    raise incorrect_type("Incorrect type given")
            return temp
        
    def __truediv__(self, o):
            if type(o)==int or type(o)==float:
                if o!=0:
                    temp=SingleLinkedList()
                    for x in self:
                        temp.addToEnd(data=x.data/o)
                    return temp
                else:
                    raise incorrect_type("Incorrect type given")
            if type(o) in tt.stype  or type(o) in tt.mtype:
                raise incorrect_type("Incorrect type given")
            elif self.length()!=o.length():
                raise incorrect_type("Incorrect type given")
            if self.head==None:
                raise incorrect_type("Incorrect type given")
            temp=SingleLinkedList()
            for start,start2 in zip(self,o):
                try:
                    temp.addToEnd(data=start.getData()/start2.getData())
                
                except:
                    raise incorrect_type("Incorrect type given")
            return temp
        
    def __floordiv__(self, o):
            if type(o)==int or type(o)==float:
                if o!=0:
                    temp=SingleLinkedList()
                    for x in self:
                        temp.addToEnd(data=x.data//o)
                    return temp
                else:
                    raise incorrect_type("Incorrect type given")
            if type(o) in tt.stype or type(o) in tt.mtype:
                raise incorrect_type("Incorrect type given")
            elif self.length()!=o.length():
                raise incorrect_type("Incorrect type given")
            if self.head==None:
                raise incorrect_type("Incorrect type given")
            temp=SingleLinkedList()
            for start,start2 in zip(self,o):
                try:
                    temp.addToEnd(data=start.getData()//start2.getData())
                
                except:
                    raise incorrect_type("Incorrect type given")
            return temp
    def __mod__(self, o):
            if type(o)==int or type(o)==float:
                if o!=0:
                    temp=SingleLinkedList()
                    for x in self:
                        temp.addToEnd(data=x.data%o)
                    return temp
                else:
                    raise incorrect_type("Incorrect type given")
            if type(o) in tt.stype or type(o) in tt.mtype:
                raise incorrect_type("Incorrect type given")
            elif self.length()!=o.length():
                raise incorrect_type("Incorrect type given")
            if self.head==None:
                raise incorrect_type("Incorrect type given")
            temp=SingleLinkedList()
            for start,start2 in zip(self,o):
                try:
                    temp.addToEnd(data=start.getData()%start2.getData())
                
                except:
                    raise incorrect_type("Incorrect type given")
            return temp
        
    def __pow__(self, o):
            if self.head==None:
                raise incorrect_type("Incorrect type given")
            temp=SingleLinkedList()
            for start in self:
                try:
                    temp.addToEnd(data=start.getData()**o)
                
                except:
                    raise incorrect_type("Incorrect type given")
            return temp
    
        
    def __eq__(self, other):
        return self.equal(other)
    
    def __gt__(self, other):
        if self.head==None and other.head==None:
            return False
        elif other.head==None:
            return False
        if type(other)!=type(self):
            raise incorrect_type("Incorrect type given")
        try:
            if self.toString("")>other.toString(""):
                return True
            else:
                return False
        except:
            raise incorrect_type("Incorrect type given")
        
    def __ge__(self,other):
        if self.head==None and other.head==None:
            return True
        elif other.head==None:
            return False
        if type(other)!=type(self):
            raise incorrect_type("Incorrect type given")
        try:
            if self.toString("")>=other.toString(""):
                return True
            else:
                return False
        except:
            raise incorrect_type("Incorrect type given")
        
    def __lt__(self, other):
        return not self.__gt__(other)
    
    def __le__(self,other):
        if self.head==None and other.head==None:
            return True
        elif other.head==None:
            return False
        if type(other)!=type(self):
            raise incorrect_type("Incorrect type given")
        try:
            if self.toString("")<=other.toString(""):
                return True
            else:
                return False
        except:
            raise incorrect_type("Incorrect type given")
    
    def __ne__(self,other):
        return not self.equal(other)
    
    def __getitem__(self, subscript):
        if isinstance(subscript, slice):
            return self.slice(start=subscript.start,end=subscript.stop,step=subscript.step)
            
        else:
            return self.nodeAtPosition(subscript)
    
    def __setitem__(self, index, value):
        return self.updateNode(self.nodeAtPosition(index),value)
    
    def __delitem__(self, index):
        return self.removeAtPosition(index)
        
    def __iter__(self):
        start=self.head
        while start:
            yield start
            start = start.getNextNode()
    def __len__(self):
        return self.length()
    
    def __hash__(self,other):
        return self.equal(other)
    
    def __str__(self,sep=" "):
        if self.head is not None:
            return "sllist([%s])" % ', '.join((str(x.data) for x in self))
        else:
            return 'sllist()'
    
    def __bool_(self):
        return False if self.isEmpty() else True
    
    def __reversed__(self):
        return self.reverse()
    
    

    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
        
    def headNode(self):
        return self.head
    
    def endNode(self):
        if self.head==None:
            return None
        else:
            return self.nodeAtPosition(self.length()-1)
        
    def iterNodes(self):
        return [i for i in self]
    
    def nodeAtPosition(self,index=None,rType=dict):
        start=self.head
        pos=0
        def node(index):
            start=self.head
            for i in range(index):
                start=start.next
            return start
        if type(index) in tt.stype:
            if index < 0 or index>=self.length():       
                raise incorrect_type("Incorrect type given")
            if type(index)!=int:
                raise incorrect_type("Incorrect type given")
            return node(index)
        elif type(index) in tt.mtype:
            if type(index)==set:
                index=list(index)
                rType=None
            d={}
            for p in index:
                if p < 0 or p>=self.length():       
                    raise incorrect_type("Incorrect type given")
                if type(p)!=int:
                    raise incorrect_type("Incorrect type given")
                d[p]=node(p)
            if rType==None or rType==dict:
                return d
            elif rType in tt.stype:
                return rType(d.values())
            else:
                raise incorrect_type("Incorrect type given")
        else:
            raise incorrect_type("Incorrect type given")
        
    def sum(self,start=None,end=None,step=None):
            if self.head==None or self.doesHaveType(str):
                raise incorrect_type("Incorrect type given")
            if start==None:
                start=0
            if end==None:
                end=self.length()-1
                endNode=None
            else:
                endNode=self.nodeAtPosition(end)
            if step==None:
                step=1
            if start>end:
                raise incorrect_type("Incorrect type given")
            
            head=self.head
            nsum=0
            for i in range(start):
                head=head.getNextNode()
            while head!=endNode:
                nsum+=head.getData()
                for i in range(step):
                    head=head.getNextNode()
                    if head==endNode:
                        break
            return nsum
    
    def mean(self):
        if self.head==None:
            raise incorrect_type("Incorrect type given")
        elif self.doesHaveType(str):
            raise incorrect_type("Incorrect type given")
        else:
            return(self.sum()/self.length())
    
    def median(self):
        if self.head==None:
            raise incorrect_type("Incorrect type given")
        elif self.doesHaveType(str):
            raise incorrect_type("Incorrect type given")
        l=self.length()
        if l==1:
            return self.head.getData()
        elif l==2:
            return self.mean()
        temp=self.new_sorted()
        if l%2!=0:
            return temp.atIndex(math.floor(l/2))
        else:
            a=temp.atIndex(l/2)
            b=temp.atIndex((l/2)-1)
            return (a+b)/2
    
    def mode(self):
        if self.head==None:
            raise incorrect_type("Incorrect type given")
        elif self.doesHaveType(str):
            raise incorrect_type("Incorrect type given")
        l=self.toList()
        m={k:l.count(k) for k in l}
        mm=[k for k,v in m.items() if v==max(m.values())]
        if len(mm)==1:
            return mm[0]
        else:
            return mm
        
    def slice(self,start=None,end=None,step=None):
            if self.head==None:
                raise incorrect_type("Incorrect type given")
            temp=SingleLinkedList()
            for x in self.iterNodes()[start:end:step]:
                temp.addToEnd(node=x)
            return temp
                
    def isUniqueType(self):
        if self.head==None:
            raise incorrect_type("Incorrect type given")
        start=self.head
        while start.getNextNode():
            if type(start.getData())==type(start.getNextNode().getData()):
                start=start.getNextNode()
                continue
            else:
                return False
        return type(self.head.getData())
    
    #Does ll have atleast one element of given Type
    def doesHaveType(self,Type=None):
        if Type==None:
            raise incorrect_type("Incorrect type given")
        
        elif Type in tt.stype:
            start=self.head
            while start:
                if type(start.getData())!=Type:
                    start=start.getNextNode()
                    continue
                else:
                    return True
            return False
        
        elif type(Type) in tt.mtype:
            o=[]
            for T in Type:
                if T in tt.stype:
                    start=self.head
                    while start:
                        if type(start.getData())!=T:
                                start=start.getNextNode()
                                continue
                        else:
                            o.append(True)
                            break
                    if start==None:
                        o.append(False)
                else:
                    raise incorrect_type("Incorrect type given")
            return o
        else:
            raise incorrect_type("Incorrect type given")
    
    # method adds elements to the starting of the Linked List
    def addToStart(self, data=None,node=None):
        if data==None and node==None:
            raise incorrect_type("Incorrect type given")
        if node==None:
            if type(data) in tt.mtype:
                for dataa in data:
                    if type(dataa) not in tt.stype:
                        raise incorrect_type("Incorrect type given")
                    tempNode = Node(dataa)
                    tempNode.setLink(self.head)
                    self.head = tempNode
                    del tempNode
                return True
        
            elif type(data) in tt.stype:
                    tempNode = Node(data)
                    tempNode.setLink(self.head)
                    self.head = tempNode
                    del tempNode
                    return True
            else:
                raise incorrect_type("Incorrect type given")
        elif data==None:
            if type(node) in tt.mtype:
                for tempNode in node:
                    if type(tempNode)!=Node:
                        raise incorrect_type("Incorrect type given")
                    tNode=tempNode.copyNode()
                    tNode.setLink(self.head)
                    self.head = tNode
                    del tNode
                return True
            elif type(node)==Node:
                    tNode=node.copyNode()
                    tNode.setLink(self.head)
                    self.head = tNode
                    del tNode
                    return True
            else:
                raise incorrect_type("Incorrect type given")
        else:
                raise incorrect_type("Incorrect type given")
        

    # method adds elements to the ending of the Linked List
    def addToEnd(self, data=None,node=None):
        if data==None and node==None:
            raise incorrect_type("Incorrect type given")
        elif self.isEmpty() and type(data) in tt.stype:
             self.addToStart(data)
             return True
        elif self.isEmpty() and type(node)==Node:
             self.addToStart(node=node)
             return True
        if node==None:
                if type(data) in tt.mtype:
                    if len(data)==0:
                        return None
                    if type(data)==set:
                            data=list(data)
                    if self.isEmpty():
                        if type(data[0]) not in tt.stype:
                            raise incorrect_type("Incorrect type given")
                        self.addToStart(data[0])
                        data=data[1:]
                    for dataa in data:
                        if type(dataa) not in tt.stype:
                            raise incorrect_type("Incorrect type given")
                        self.endNode().setLink( Node(dataa))
                        
                elif type(data) in tt.stype:
                        self.endNode().setLink(Node(data))
                else:
                    raise incorrect_type("Incorrect type given")
                return True
        elif data==None:
            if type(node) in tt.mtype:
                    if type(node)==set:
                            node=list(node)
                    if self.isEmpty():
                        if type(node[0])!=Node:
                            raise incorrect_type("Incorrect type given")
                        self.head=node[0].copyNode()
                        node=node[1:]
                    for nd in node:
                            if type(nd)!=Node:
                                raise incorrect_type("Incorrect type given")
                            self.endNode().setLink(nd.copyNode())
            elif type(node)==Node:
                    self.endNode().setLink(node.copyNode())
            else:
                    raise incorrect_type("Incorrect type given")
            return True
        else:
            raise incorrect_type("Incorrect type given")
            
    
    def addToPosition(self,data=None,index=None,node=None):
        if type(node) in tt.mtype or type(data) in tt.mtype:
            raise incorrect_type("Incorrect type given")
        def ins(nd,index,headNode):
                if index < 0 or index>self.length():       
                    raise incorrect_type("Incorrect type given")
                if index == 0:
                    self.addToStart(data)
                    return True
                else:
                    for i in range(index-1):
                         headNode = headNode.getNextNode()
                    newNode = nd
                    newNode.setLink(headNode.getNextNode())
                    headNode.setLink(newNode)
                    return True
        if node==None:
            if type(data)==dict:
                for index,data in sorted(data.items()):
                        ins(Node(data),index,self.head)
            elif type(data) in tt.stype:
                        ins(Node(data),index,self.head)
            else:
                raise incorrect_type("Incorrect type given")
        elif data==None:
            if type(node)==dict:
                for index,node in sorted(node.items()):
                        ins(node,index,self.head)
            elif type(node)==Node:
                        ins(node,index,self.head)
            else:
                raise incorrect_type("Incorrect type given")
    
    #does linked list has given node or not?
    def isNodeIn(self,node=None):
        if node==None:
            raise incorrect_type("Incorrect type given")
        return True if node in self else  False

    

    def datanode(self,data):
        for head in self:
            if head.getData()==data:
                return head
        return None


    #insert after given node
    def insertAfter(self, ref_node=None, data=None, nodes=None):
            if ref_node is None or self.isEmpty():
                raise incorrect_type("Incorrect type given")
            if not self.isNodeIn(ref_node):
                raise incorrect_type("Incorrect type given")    
            if nodes==None:
                if type(data) in tt.stype:
                    new_node = Node(data)
                    new_node.setLink(ref_node.getNextNode())
                    ref_node.setLink(new_node)
                    return True
                elif type(data) in tt.mtype:
                    for dataa in data:
                        if type(dataa) not in tt.stype:
                            raise incorrect_type("Incorrect type given")
                        new_node = Node(dataa)
                        new_node.setLink(ref_node.getNextNode())
                        ref_node.setLink(new_node)
                        ref_node=new_node
                    return True
                else:
                    raise incorrect_type("Incorrect type given")
            
            elif data==None:
                if type(nodes)==Node:
                    new_node = nodes.copyNode() 
                    new_node.setLink(ref_node.getNextNode())
                    ref_node.setLink(new_node) 
                    return True
                elif type(nodes) in tt.mtype:
                    for node in nodes:
                        if type(node)!=Node:
                            raise incorrect_type("Incorrect type given")
                        new_node = node.copyNode()
                        new_node.setLink(ref_node.getNextNode())
                        ref_node.setLink(new_node)
                        ref_node=new_node
                    return True
                else:
                    raise incorrect_type("Incorrect type given")
            else:
                    raise incorrect_type("Incorrect type given")

    # method returns length of linked list
    def length(self):
        start = self.head
        size = 0
        while start:
            size += 1
            start = start.getNextNode()
        return size

    # method returns index of the recieved data
    def index(self, data=None,rType=dict):
        if data==None:
            raise incorrect_type("Incorrect type given")
        start = self.head
        position = 0
        if type(data) in tt.stype:
            while start:
                if start.getData() == data:
                    return position
                else:
                    position += 1
                    start = start.getNextNode()
            return -1
        elif type(data) in tt.mtype:
            if type(data)==set:
                data=list(data)
            d={}
            for dataa in data:
                if type(dataa) not in tt.stype:
                    raise incorrect_type("Incorrect type given")
                d[dataa]=None
                start = self.head
                position = 0
                for i in range(self.length()):
                    if start.getData() == dataa:
                        d[dataa]=position
                        break
                    else:
                        position += 1
                    start = start.getNextNode()
                if d[dataa]==None:
                    d[dataa]=-1
            if rType==None or rType==dict:
                return d
            elif rType in tt.mtype:
                return rType(d.values())
            else:
                raise incorrect_type("Incorrect type given")
        else:
            raise incorrect_type("Incorrect type given")

 # method returns the element at given position
    def atIndex(self, index,rType=dict):
        start=self.head
        pos=0
        if type(index) in tt.stype:
            if index < 0 or index>=self.length():       
                raise incorrect_type("Incorrect type given")
            if type(index)!=int:
                raise incorrect_type("Incorrect type given")
            return self.nodeAtPosition(index).data
    
        elif type(index) in tt.mtype:
            if type(index)==set:
                index=list(index)
                rType=None
            d={}
            for p in index:
                if p < 0 or p>=self.length():       
                    raise incorrect_type("Incorrect type given")
                if type(p)!=int:
                    raise incorrect_type("Incorrect type given")
                d[p]=self.nodeAtPosition(index).data
            if rType==None or rType==dict:
                return d
            elif rType in tt.stype:
                return rType(d.values())
            else:
                raise incorrect_type("Incorrect type given")
        else:
            raise incorrect_type("Incorrect type given")
            
    def replace(self,data=None,New_data=None,All=True):
        if data==None or type(data)==set or type(New_data)==set:
            raise incorrect_type("Incorrect type given")
        elif New_data==None :
            if type(data)!=dict:
                raise incorrect_type("Incorrect type given")
        def rep(data,New_data,All):
            start=self.head
            while start:
                if start.getData() == data:
                        start.updateData(New_data)
                        if not All:
                            return None
                else:
                    start = start.getNextNode()
        if type(data) in tt.stype:
                rep(data,New_data,All)
                
        elif type(data) in tt.mtype and type(New_data) in tt.mtype and len(data)==len(New_data):
                for d,n in zip(data,New_data):
                    if type(d) in tt.stype and type(n) in tt.stype:
                        rep(d,n,All)
        elif type(data)==dict and New_data==None:
            for k,v in data.items():
                rep(k,v,All)
        else:
            raise incorrect_type("Incorrect type given")
    
    def updateNode(self,node=None,data=None):
        if node==None or not self.isNodeIn(node) or data==None or type(data) in tt.mtype:
            raise incorrect_type("Incorrect type given")
        elif type(data) in tt.stype:
            node.updateData(data)
        else:
            raise incorrect_type("Incorrect type given")
                
    # method removes item passed from the Linked List
    def removeItem(self,item=None,All=True,node=None):
        if item==None and node==None:
            raise incorrect_type("Incorrect type given")
        if node==None:
            def rmv(item):
                start = self.head
                previous = None
                found = False
                while not found and start:
                    if start.getData() == item:
                        found = True
                    else:
                        previous = start
                        start = start.getNextNode()
        
                # if previous is None then the data is found at first position
                if found:
                    if previous is None:
                        self.head = start.getNextNode()
                    else:
                        previous.setLink(start.getNextNode())
                return found
            if type(item) in tt.stype:
                if All:
                    while rmv(item):
                        pass
                else:
                    rmv(item)
            elif type(item) in tt.mtype:
                for data in item:
                    if type(data) not in tt.stype:
                        raise incorrect_type("Incorrect type given")
                    if All:
                        while rmv(data):
                            pass
                    else:
                        rmv(item)
            else:
                raise incorrect_type("Incorrect type given")
        elif item==None:
            if not self.isNodeIn(node):
                raise incorrect_type("Incorrect type given")
            def rmv(node):
                start=self.head
                if start==node:
                    self.removeAtStart()
                    return True
                prev=start
                start=start.getNextNode()
                while start:
                    if start==node:
                        temp=start
                        prev.setLink(temp.getNextNode())    
                        del temp
                        return True
            if type(node) in tt.mtype:
                for nd in node:
                    if type(nd)!=Node:
                        raise incorrect_type("Incorrect type given")
                    rmv(nd)
            elif type(node)==Node:
                if type(node)!=Node:
                        raise incorrect_type("Incorrect type given")
                rmv(node)
                
    # method returns max element from the List
    def Max(self):
        if self.head==None:
            raise incorrect_type("Incorrect type given")
        start = self.head
        largest = start.getData()
        while start:
            if largest < start.getData():
                largest = start.getData()
            start = start.getNextNode()
        return largest
    
    def remove_Max(self,All=True):
            self.removeItem(self.Max(),All)

    # method returns minimum element of Linked list
    def Min(self):
        if self.head==None or not self.isUniqueType():
            raise incorrect_type("Incorrect type given")
        start = self.head
        smallest = start.getData()
        while start:
            if smallest > start.getData():
                smallest = start.getData()
            start = start.getNextNode()
        return smallest
    
    def remove_Min(self,All=True):
            self.removeItem(self.Min(),All)

    # method pushes element to the Linked List
    def push(self, data):
        self.addToEnd(data)
        return True

    # method removes and returns the last element from the Linked List
    def popEnd(self,No_of_times=1,rType=list):
        if type(No_of_times)!=int or No_of_times>self.length() or No_of_times<1:
            raise incorrect_type("Incorrect type given")
        if rType not in tt.mtype:
            raise incorrect_type("Incorrect type given")
        a=[]
        for i in range(No_of_times):
                start = self.head
                previous = None
                while start.getNextNode():
                    previous = start
                    start = start.getNextNode()
                if previous is None:
                    self.head = None
                else:
                    previous.setLink(None)
                    data = start.getData()
                    del start
                    a.append(data)
        if rType==None and No_of_times==1:
            return a[0]
        if rType in tt.mtype:
            if rType==None:
                rType=list
            return rType(a)
        else:
                raise incorrect_type("Incorrect type given")

    # method returns a copy of the current Linked List
    def copy(self):
        if self.head is None:
             return None
        temp = SingleLinkedList()
        for x in self:
            temp.addToEnd(x.getData())
        return temp

    # method to clear LinkedList
    def clear(self):
        while (self.head != None):
              temp = self.head
              self.head = self.head.getNextNode()
              del temp
        return True

    # method returns and removes element at recieved position
    def removeAtPosition(self, index=None):
        if index==None:
            raise incorrect_type("Incorrect type given")
        def rmv(index,headNode):
                if index < 0 or index>=self.length():       
                    raise incorrect_type("Incorrect type given")
                if index == 0:
                    self.removeAtStart()
                    return True
                else:
                    temp = self.head
                    for i in range(index-1):
                        temp = temp.getNextNode()
                    temp2 = temp.getNextNode().getNextNode()
                    a=temp.getNextNode()
                    temp.setLink(temp2)
                    del a
                    return True
        if type(index) in tt.stype:
                    rmv(index,self.head)
        elif type(index) in tt.mtype:
                for pos in sorted(index,reverse=True):
                    rmv(pos,self.head)
        else:
            raise incorrect_type("Incorrect type given")

    
    #remove at start
    def removeAtStart(self,No_of_Nodes=1):
        if type(No_of_Nodes)!=int:
            raise incorrect_type("Incorrect type given")
        if No_of_Nodes>self.length():
            raise incorrect_type("Incorrect type given")
        for i in range(No_of_Nodes):
            if not self.head:
                return None
            temp = self.head
         
            # Move the head pointer to the next node
            self.head = self.head.getNextNode()
            del temp
        return self.head
        
        
    def removeAtEnd(self,No_of_Nodes=1):
        if type(No_of_Nodes)!=int:
            raise incorrect_type("Incorrect type given")
        if No_of_Nodes>self.length():
            raise incorrect_type("Incorrect type given")
        for i in range(No_of_Nodes):
            start = self.head
            previous = None
            while start.getNextNode():
                previous = start
                start = start.getNextNode()
            if previous is None:
                self.head = None
            else:
                previous.setLink(None)
                del start
        return True
    
    def merge(self,start):
        if start==None and self.head==None:
            return SingleLinkedList()
        elif start==None:
            return self
        else:
            try:
                self.addToEnd(start.toList())
            except:
                raise incorrect_type("Incorrect type given")

    # method returns string of elements of Linked list
    # the Elements are seperated by seperator if passed else all elements are appended
    def toString(self, seperator=" "):
        if type(seperator)!=str:
            raise incorrect_type("Incorrect type given")
        start = self.head
        finalString = ""
        while start:
            tempString = start.getData()
            finalString += str(tempString)
            start = start.getNextNode()
            # if next node exists only the append seperator
            if start:
                finalString += seperator

        return finalString

    # method returns count of Element recieved
    def dataCount(self,data,rType=dict):
        start = self.head
        count1 = 0
        if type(data) in tt.stype:
            while start:
                if start.getData() == data:
                    count1 += 1
                start = start.getNextNode()
            return count1
    
        elif type(data) in tt.mtype:
            if type(data)==set:
                data=list(data)
                rType=dict
            d={}
            for p in data:
                if type(p) not in tt.stype:
                    raise incorrect_type("Incorrect type given")
                start = self.head
                d[p] = 0
                while start:
                    if start.getData() == p:
                        d[p]+=1
                    start = start.getNextNode()
            if rType==None or rType==dict:
                return d
            elif rType in tt.stype:
                return rType(d.values())
            else:
                raise incorrect_type("Incorrect type given")
        else:
            raise incorrect_type("Incorrect type given")
            
    def count(self):
        Count_dict = dict()
        if self.isEmpty():
            return Count_dict
        else:
            for item in self:
                if item.data in Count_dict.keys():
                    Count_dict[item.data] +=1
                else:
                    Count_dict[item.data] =1
        return Count_dict
        

    # method returns builtin List of python consisting of Elements of LinkedList
    def toList(self):
        return [x.data for x in self]

    # method returns builtin Set of python consisting of Elements of LinkedList
    def toSet(self):
        return {x.data for x in self}

    # method reverses the LinkedList
    def reverse(self):
        if self.head==None:
            return True
        temp=self.copy()
        start = temp.headNode()
        tempNode = None
        previousNode = None

        while start:
            tempNode = start.getNextNode()
            start.setLink(previousNode)
            previousNode = start
            start = tempNode

        self.head = previousNode
        return self
    
    def removeDuplicates(self):
        if self.head==None:
            raise incorrect_type("Incorrect type given")
        prev=None
        start=self.head
        s=set()
        while start:
            if start.getData() not in s:
                s.add(start.getData())
                prev=start
                start=start.getNextNode()
            else:
                temp=start
                prev.setLink(start.getNextNode())
                start.setLink(None)
                del temp
                start=prev.getNextNode()
                
    def equal(self,llist=None):
        if llist==None and self.head==None:
            return True
        elif llist==None:
            return False
        if type(llist)!=type(self):
            raise TypeError("Incorrect type given")
        try:
            if self.toString("")==llist.toString(""):
                return True
            else:
                return False
        except:
            raise incorrect_type("Incorrect type given")
    
    def search(self,data=None,rType=dict):
        if data==None:
            raise incorrect_type("Incorrect type given")
        if type(data) in tt.stype:
            if self.datanode(data):
                return True
            else:
                return False
        elif type(data) in tt.mtype or type(data)==dict:
                d={}
                if type(data)==set:
                    rType=dict
                for dataa in data:
                    if type(dataa) in tt.stype:
                        if self.datanode(dataa):
                            d[dataa]=True
                        else:
                            d[dataa]=False
                if rType in tt.mtype or rType==dict:
                        return rType(d)
                else:
                        raise incorrect_type("Incorrect type given")
        else:
            raise incorrect_type("Incorrect type given")
                        
    # method that sorts LinkedList
    def sorted(self,reverse=False):
        if self.head==None:
            return True
        start = self.head
        beginNode = start
        while beginNode:
                tempNode = beginNode
                tempNode2 = beginNode
                smallest = beginNode.getData()
                while tempNode:
                    if smallest > tempNode.getData():
                        smallest = tempNode.getData()
                        tempNode2 = tempNode
                    tempNode = tempNode.getNextNode()
    
                # swap data of beginNode and tempNode2
                temp = beginNode.getData()
                beginNode.updateData(tempNode2.getData())
                tempNode2.updateData(temp)
                beginNode = beginNode.getNextNode()
        if reverse:
            self.reverse()
        return self
            
    # method returns new instance of the sorted LinkedList without changing original LinkedList
    def new_sorted(self,reverse=False):
        temp=self.copy()
        temp.sorted(reverse)
        return  temp
    
    def isSorted(self,reverse=False):
        if self.head==None:
            raise incorrect_type("Incorrect type given")
        start=self.head
        while start.getNextNode():
            if reverse:
                if start.getData()>=start.getNextNode().getData():
                    pass
                else:
                    return False
            else:
                if start.getData()<=start.getNextNode().getData():
                    pass
                else:
                    return False
            start=start.getNextNode()
        return True
    
    def sortedAssign(self,data=None,reverse=False):
        if data==None or self.head==None:
            raise incorrect_type("Incorrect type given")
        if not self.isSorted(reverse):
            self.sorted(reverse)
        def func(data=None,reverse=False):
            start=self.head
            prev=None
            while start:
                if reverse:
                    if start.getData()<=data:
                        temp=Node(data)
                        if prev==None:
                            self.addToStart(data)
                        else:
                            prev.setLink(temp)
                            temp.setLink(start)
                        del temp
                        return None
                    prev=start
                    start=start.getNextNode()
                else:
                    if start.getData()>=data:
                        temp=Node(data)
                        if prev==None:
                            self.addToStart(data)
                        else:
                            prev.setLink(temp)
                            temp.setLink(start)
                        del temp
                        return None
                    prev=start
                    start=start.getNextNode()
        if type(data) in tt.stype:
                func(data,reverse)
            
        elif type(data) in tt.mtype:
                for dataa in data:
                    if type(dataa) in tt.stype:
                            func(dataa,reverse)
                    else:
                        raise incorrect_type("Incorrect type given")
        else:
            raise incorrect_type("Incorrect type given")
            
    def sumTwoLlist(self,str1, str2):
        if (len(str1) > len(str2)):
            t = str1;
            str1 = str2;
            str2 = t;
        Str = "";
        n1 = len(str1);
        n2 = len(str2);
        str1 = str1[::-1];
        str2 = str2[::-1];
        carry = 0;
        for i in range(n1):
            sum = int(str1[i])+int(str2[i])+carry;
            Str += str(sum % 10);
            carry = int(sum / 10);
        for i in range(n1, n2):
            sum = int(str2[i])+carry;
            Str += str(sum % 10);
            carry = int(sum / 10);
        if (carry):
            Str += str(carry);
        self.addToEnd(data=[x for x in Str[::-1]])
        return self
    
    
    def diffTwoLlist(self,str1, str2):
        flag=0
        if float(str1)<float(str2):
            str1, str2 = str2, str1
            flag=1
        Str = ""
        n1 = len(str1)
        n2 = len(str2)
        diff = n1 - n2
        carry = 0
        for i in range(n2 - 1, -1, -1):
            sub = int(str1[i + diff]) -int(str2[i]) - carry
            if (sub < 0):
                sub += 10
                carry = 1
            else:
                carry = 0
            Str += str(sub)
        for i in range(n1 - n2 - 1, -1, -1):
            if (str1[i] == '0' and carry):
                Str += '9'
                continue
            sub = int(str1[i]) - carry
            if (i > 0 or sub > 0):
                Str += str(sub)
            carry = 0
        self.addToEnd(data=[x for x in Str[::-1]])
        if flag:
            self.addToStart(data="-")
        return self
    
  
    def __minusCheck(self,first,second):
        flag=0
        p=-1
        def point(first,second):
            i=len(first)-first.index(".")-1 if first.index(".")>-1 else -1
            j=len(first)-second.index(".")-1 if second.index(".")>-1 else -1
            if i<0 and j<0:
                return None
            elif i>0 and j>0:
                return i+j
            else:
                return i if j<0 else j

        if type(first)==str and type(second)==str:
            if len(first)==0 and len(second)==0:
                return SingleLinkedList(),SingleLinkedList(),0
            else:
                try:
                        first=SingleLinkedList(data=[x for x in first])
                        second=SingleLinkedList(data=[x for x in second])
                except:
                    raise incorrect_type("Incorrect type given")
        if type(first)==SingleLinkedList and type(second)==SingleLinkedList:
            if first.head==None or second.head==None:
                return SingleLinkedList()
            else:
                if first[0].data=="-" and second[0].data!="-":
                        p=point(first,second)
                        m=first[1::]
                        n=second
                        flag=1
                elif first[0].data!="-" and second[0].data=="-":
                        p=point(first,second)
                        m=first
                        n=second[1::]
                        flag=1
                elif first[0].data=="-" and second[0].data=="-":
                        p=point(first,second)
                        m=first[1::]
                        n=second[1::]
                else:
                        p=point(first,second)
                        m=first
                        n=second
        else:
            raise incorrect_type("Incorrect type given") 
        return m,n,flag,p
    
    
    def multiplyTwoList(self,first, second):
        if type(first)!=str and type(second)!=str and type(first)!=SingleLinkedList and type(second)!=SingleLinkedList:
            raise incorrect_type("Incorrect type given") 
        m,n,flag,p=self.__minusCheck(first, second)
        result=SingleLinkedList()
        result.addToEnd(data=0)
        result= result*(len(m)+len(n)+1)
        temp=result.head
        for x in n[::-1]:
            try:
                if x.data==".":
                    continue
                x=int(x.data)
                if x>9:
                    raise incorrect_type("Incorrect type given") 
                carry = 0
                temp2 = temp
                for y in m[::-1]:
                    if y.data==".":
                        continue
                    y=int(y.data)
                    if y>9:
                        raise incorrect_type("Incorrect type given") 
                    mul = ((y*x) + carry)
                    temp2.data += mul % 10
                    carry = ((mul // 10) + (temp2.data // 10))
                    temp2.data = temp2.data % 10
                    temp2 = temp2.next
                if(carry > 0):
                    temp2.data += carry
                temp = temp.next
            except:
                raise incorrect_type("Incorrect type given")
        result.reverse()
        start = result.head
        while(start.data == 0):
            result.head = start.next
            start = start.next
        self+=result
        if flag:
            self.addToStart("-")
        
        if p:
            self.addToPosition(data=".",index=len(self)-p)
        return self
  
                    
                
# node class
class Node:
    # default value of data and link is none if no data is passed
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return "sllnode(%s)" % str(self.data)
    
    def __iadd__(self,o):
        try:
            self.updateData(self.data+o.data)
        except:
            raise incorrect_type("Incorrect type given")

    # method to update the data feild of Node
    def updateData(self, data):
        self.data = data

    # method to set next feild the Node
    def setLink(self, node):
        self.next = node

    # method returns data feild of the Node
    def getData(self):
        return self.data

    # method returns address of the next Node
    def getNextNode(self):
        return self.next
    #return copy of the node
    def copyNode(self):
        return Node(self.getData())