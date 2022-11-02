class bike:
    def __init__(self,bike_name,cost_in_lakhs):
        self.name=bike_name
        self.cost=cost_in_lakhs
        
    def show(self):
        print(f"{self.name} costs {self.cost} lakhs ")
    
def sportsbike(bike):
    def __init__(self):
        super.__init__()
    
    def maxspeed(bike,speed):
        print(f"the max speed of bike is {speed}")


honda=bike("honda",56)
honda.show()
kawasaki=sportsbike("kawasaki",100)
kawasaki.show()
kawasaki.maxspeed(430)