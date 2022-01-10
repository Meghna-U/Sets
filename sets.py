var1=set()
var2=set()
size1=int(input("Enter size of first set:"))
i=1
while i<=size1:
    n=int(input("Enter number "+str(i)+" in first set:"))
    var1.add(n)
    i+=1
size2=int(input("Enter size of second set:"))
j=1
while j<=size2:
    n=int(input("Enter number "+str(j)+" in second set:"))
    var2.add(n)
    j+=1
print("Set 1:",var1)
print("Set 2:",var2)
var3=var1.union(var2)
print("Union of sets:",var3)
var4=var1.intersection(var2)
print("Intersection of sets:",var4)
var5=var1.difference(var2)
print("Difference of sets:",var5)
var6=var1.symmetric_difference(var2)
print("Symmetric difference of sets:",var6)
