#single inheritence
class parent:
    def mobile(self):
        print("pad mobile")
class child (parent):
    def nomobile(self):
        print("no mobile")
surya=child()
surya.mobile()