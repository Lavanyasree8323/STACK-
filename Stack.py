class stack:
    def __init__(self):
        self.st=[]
# creating the stack operation using method name
    def isempty(self):
        return self.st==[]
    def push(self,element):
        self.st.append(element)
    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.st.pop()
# peep- It returns the topmost element without deleting it from the stack
    def peep(self):
        n=len(self.st)
        return self.st[n-1]
    def search(self,element):
        if self.isempty():
            return -1
        else:
            try:
                n=self.st.index(element)
                return len(self.st)-n
            except ValueError:
                return -2
    def display(self):
        return self.st
