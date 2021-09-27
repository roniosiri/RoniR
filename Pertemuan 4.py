class ninja:
    def __init__(self, nama, lulusan, cakra, klan):
        self.nama = nama
        self.lulusan = lulusan
        self.cakra = cakra
        self.klan = klan

    def printname(self):
        print(self.nama)
        print(self.lulusan)
        print(self.cakra)
        print(self.klan)

class suv(ninja):
    def __init__(self, nama, lulusan, cakra, klan):
        ninja.__init__(self, nama, lulusan, cakra, klan)
        self.pangkat= "genin"
        
    def tampilansuv(self):
        print("nama     : ", self.nama)
        print("lulusan  : ", self.lulusan)
        print("pangkat  : ", self.pangkat)
        print("cakra    : ", self.cakra)
        print("klan     : ", self.klan)
        
        

class mvp(ninja):
    def __init__(self, nama, lulusan, cakra, klan):
        ninja.__init__(self, nama, lulusan, cakra, klan)
        self.pangkat= "cunin"
    
    def tampilanmvp(self):
        print("nama     : ", self.nama)
        print("lulusan  : ", self.lulusan)
        print("pangkat  : ", self.pangkat)
        print("cakra    : ", self.cakra)
        print("klan     : ", self.klan)
        
x = suv("sahril", 2020, "api", "uciha")
y = mvp("arjuna", 2013, "bumi", "uzumaki")
b = mvp("aden", 2016, "udara", "nara")

x.tampilansuv()
print("---------------------")
y.tampilanmvp()
print("---------------------")
b.tampilanmvp()