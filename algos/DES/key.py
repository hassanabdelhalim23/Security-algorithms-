from algos.DES.matrix import *
class key:
    allkey=list()
    Key=""
    C0=""
    D0=""
    key_pin=""
    object=matrix()
    def __init__(self,key):
        self.Key=key
    def keytoPin(self):
        text_ip=""
        for i in range(len(self.Key)):
            text_ip=text_ip+self.object.hex2binarary(self.Key[i])
        self.key_pin=text_ip
    def KEyPC1(self):
        text_ip=""
        for i in range(self.object.PC1.__len__()):
            text_ip=text_ip+self.key_pin[self.object.PC1[i]-1]
        self.key_pin=text_ip

    def rounds(self):

        self.C0=self.key_pin[0:28]
        self.D0=self.key_pin[28:56]
        shiftAmount = "1122222212222221";
        for i in range(len(shiftAmount)):
            if shiftAmount[i] =="1":
                self.C0=self.C0[1:28]+self.C0[0:1]
                self.D0=self.D0[1:28]+self.D0[0:1]


            else:
                self.C0=self.C0[2:28]+self.C0[0:2]
                self.D0=self.D0[2:28]+self.D0[0:2]

            self.allkey.append((self.C0+self.D0))
        return self.allkey
