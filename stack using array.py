class stack:
    def _init_(self,val):
        self.val=val
        self.top=-1
        self.arr=[None]*val
    def is_empty(self):
        return self.top==-1
    def is_full(self):
        return self.top==self.val-1
    def push(self,ele):
        if self.is_full():
            print("over flow")
            return
        else:
            self.top+=1
            self.arr[self.top]=ele
    def pop(self):
        if self.is_empty():
            print("Under flow")
            return None
        else:
            ele=self.arr[self.top]
            self.top-=1
            return ele
    def peek(self):
        return self.arr[self.top]
n=int(input())
stack=stack(n)
while True:
    c=int(input())
    if c==1:
        ele=int(input())
        stack.push(ele)
    elif c==2:
        res=stack.pop()
        print(res)
    elif c==3:
        res=stack.peek()
        print(res)
    elif c==4:
        print("exit")
        break
    else:
        print("invalid input")
