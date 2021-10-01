


class ninja:
    def intro(self): 
        print ("setiap ninja memilki tingkatan dan cakra yang berbeda")
    def jenis1(self):
        print ("ini adalah tingkatannya :")
    def jenis2(self):
        print (" ini adalah cakranya :")

class tingkatan:
    def genin(self):
        print("1.genin merupakan tingkatan terendah setingkat sd ")
    def chunin(self):
        print("2.chunin bisa dikatakan setingkat dengan smp")
    def jounin(self):
        print("3.jounin setingkat seperti sma")

class cakra:
    def air(self):
        print("-cakra air")
    def api(self):
        print("-cakra api")
    def bumi(self):
        print("-cakra bumi")
    def petir(self):
        print("-cakra petir")
    def angin(self):
        print("-cakra angin")

class genin:
    def __init__(self, nama, cakra):
        self.nama = nama
        self.cakra = cakra
        
    def bersuara(self):
        print("saya adalah seorang genin. nama saya",self.nama,"dan cakraku",self.cakra)
        
class chunin:
    def __init__(self, nama, cakra):
        self.nama = nama
        self.cakra = cakra
        
    def bersuara(self):
        print("saya chunin hahah. nama saya",self.nama,"cakra aku adalah",self.cakra)

class jounin:
    def __init__(self, nama, cakra):
        self.nama = nama
        self.cakra = cakra
        
    def bersuara(self):
        print("aku adalah jounin, nama",self.nama,",cakra yaitu",self.cakra)
        
genin1= genin("alexander", "angin")
chunin1= chunin("ucup", "api dan air")
jounin1= jounin("abdul", "petir")

        
        
obj_ninja = ninja()
obj_tingkatan = tingkatan()
obj_cakra = cakra()

obj_ninja.intro()
print("=========================")
obj_ninja.jenis1()
obj_tingkatan.genin()
obj_tingkatan.chunin()
obj_tingkatan.jounin()
print("=========================")
obj_ninja.jenis2()
obj_cakra.angin()
obj_cakra.air()
obj_cakra.bumi()
obj_cakra.api()
obj_cakra.petir()
print("\n")

for ninja in (genin1, chunin1, jounin1):
    ninja.bersuara()

