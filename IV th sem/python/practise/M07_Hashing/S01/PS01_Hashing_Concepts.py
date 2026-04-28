a=10
b='Kalyani'
c=3.454
print(hash(a))
print(hash(b))
print(hash(c))

size = 7
table[None]*size
a=[10,20,30]
for key in a:
    hash_key=key%size
    '''
    1.count Frequency of Elements(using)'''
    def merge(left,right):
        i=j=0
        result=[]
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result+=left[i:]
        result+=right[j:]
        return result
    