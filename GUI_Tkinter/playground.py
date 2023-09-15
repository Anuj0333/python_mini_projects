def sum(*args):
    add=0
    for i in args:
        add+=i
    return add

# print(sum(5,8,9,4,3,1))



def cal(n,**kwargs):
    # for key,value in kwargs.items():
        # print(key)
        # print(value)
        # n+=kwargs["add"]
        n-=kwargs["sub"]
        n*=kwargs["multiply"]
        # print(n)

cal(5,add=8,sub=5,multiply=4)

class car:
     def __init__(self,**kw) :
          self.model=kw["model"]
          self.make=kw["make"]
          self.color=kw.get("color")
          self.seats=kw.get("seats")

my_car=car(make="ford",model="GT-R",color="black")
print(my_car.make,my_car.seats)


