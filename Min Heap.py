#Time Complexity:: getMin() - O(1), bubbleUp(): O(logn), bubbleDown(): O(logn) ,insert(): O(logn) , extractMin():O(logn)  
#Space Complexity:: O(n) where n is the maximum number of elements in the array
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Minheap:
    def __init__(self):
       self.heap=[]
    
    def getMin(self):
        return self.heap[0] #O(1) operation peaking the root of the tree
    
    def bubbleUp(self, index):
        parentIndex = (index-1)//2 #formula to find parent node
        if parentIndex<0: #to prevent from going to outofbound
            return
        
        if self.heap[parentIndex]<self.heap[index]:
            return #to check if bubble up is done
        
        #a,b = b,a reassigning variables
        self.heap[parentIndex],self.heap[index]=self.heap[index],self.heap[parentIndex]
        self.bubbleUp(parentIndex) 
        
    def bubbleDown(self,index):
        leftchild = 2*index + 1 #formula for finding leftchild of bubbledown index
        rightchild = 2*index + 2 #formula for finding rightchild of bubbledown index
        
        temp = index #passing index of node to bubble down
        
        if leftchild<len(self.heap) and self.heap[temp]>self.heap[leftchild]:
            temp = leftchild #leftchild is smaller than index so it becomes temp
        if rightchild<len(self.heap) and self.heap[temp]>self.heap[rightchild]:
            temp = rightchild #rightchild is smaller than index/leftchild so it becomes temp
        if temp == index:
            return #if no smaller values in the child nodes then return
        self.heap[temp], self.heap[index] = self.heap[index],self.heap[temp] #swap the nodes
        self.bubbleDown(temp) #recursive function call till temp==index
        
    def insert(self,key):
        self.heap.append(key) #add element to end of heap array
        self.bubbleUp(len(self.heap)-1) #bubbleup the element at the end of the array
            
    def extractMin(self):
        self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0] #swap root node with leaf node
        temp = self.heap.pop() #pop the leaf node
        self.bubbleDown(0) #bubble down root node
        return temp
        
    def size(self):
        return len(self.heap)

h=Minheap()
h.insert(5);
h.insert(3);
h.insert(17);
h.insert(11);
h.insert(79);
h.insert(19);
h.insert(6);
h.insert(25);
h.insert(9);
print(h.heap)
print("Minimum:", h.getMin())
for i in range(len(h.heap)):
    print(h.extractMin())
