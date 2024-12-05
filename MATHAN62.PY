#Multilevel inheritance
class granddad:
    def mobile():
        print("grand mobile")
class father(granddad):
    def dad():
        print("dads moobile")
class son (father):
    pass
s1=son
s1.dad()
s1.mobile()                
