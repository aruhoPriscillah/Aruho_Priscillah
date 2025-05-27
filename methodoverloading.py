class Math:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return a
            
m = Math()
print(m.add(2, 3))      # Output: 5
print(m.add(1, 2, 3))   # Output: 6
