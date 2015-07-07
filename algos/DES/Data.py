from itertools import permutations
from algos.DES.matrix import *
from algos.DES.key import *
class DESdata:
    finalRandL=""
    Key=""
    Text=""
    Keysafterpermulation=list()
    RofRounds=list()
    LofRounds=list()
    Keys=list()
    Text_bin=""
    R=""
    L=""
    object1=key
    object =matrix()
    def __init__(self,Key,text):
        self.Key=Key
        self.Text=text
        self.object1=key(self.Key)

        for i in range(len(self.Text)):
           self.Text_bin=self.Text_bin+self.object.hex2binarary(self.Text[i])


    def ROunds(self):
        for X in self.Keys:
            tempL=self.L
            self.L=self.R


            selectio=self.selection_table(self.R)


            KEYperm=self.KEYPC2(X)
            self.Keysafterpermulation.append(KEYperm)
            xoroutput=self.XOR(selectio,KEYperm)

            sboxoutput=self.SBOX(xoroutput)

            permuateSbox=self.permuate(sboxoutput)
            self.R=self.XOR(permuateSbox,tempL)
            self.LofRounds.append(self.L)
            self.RofRounds.append(self.R)



    def KEYPC2(self,KEY):
        text_ip=""
        for i in range(self.object.PC2.__len__()):
            text_ip=text_ip+KEY[self.object.PC2[i]-1]
        return text_ip


    def permuate(self,text):
        text_ip=""
        for i in range(self.object.permuate_p.__len__()):
            text_ip=text_ip+text[self.object.permuate_p[i]-1]
        return text_ip

    def SBOX(self,RSBOX):
        index=0
        temp=""
        m=""
        for i in range(len(RSBOX)):
          if i%6==5:
              temp=temp+RSBOX[i]
              row=0
              col=0
              row =(int)(self.object.binary2dex(temp[0:1] + temp[5:6]))
              col=(int)(self.object.binarary27ex_sbox(temp[1:5]))
              if index ==0:
                  temp_val=self.object.s1[row][col]
                  m=m+self.object.ex2binary(str(temp_val))
              if index ==1:
                  temp_val=self.object.s2[row][col]
                  m=m+self.object.ex2binary(str(temp_val))
              if index ==2:
                  temp_val=self.object.s3[row][col]
                  m=m+self.object.ex2binary(str(temp_val))
              if index ==3:
                  temp_val=self.object.s4[row][col]
                  m=m+self.object.ex2binary(str(temp_val))
              if index ==4:
                  temp_val=self.object.s5[row][col]
                  m=m+self.object.ex2binary(str(temp_val))
              if index ==5:
                  temp_val=self.object.s6[row][col]
                  m=m+self.object.ex2binary(str(temp_val))
              if index ==6:
                  temp_val=self.object.s7[row][col]
                  m=m+self.object.ex2binary(str(temp_val))
              if index ==7:
                  temp_val=self.object.s8[row][col]
                  m=m+self.object.ex2binary(str(temp_val))




              index=index+1
              temp=""
          else:
              temp=temp+RSBOX[i]

        return m


    def init_ip(self):
        text_ip=""
        for i in range(len(self.Text_bin)):
            text_ip=text_ip+self.Text_bin[self.object.ip[i]-1]
        self.Text_bin=text_ip
    def intit_R0andL0(self):
        self.L=self.Text_bin[0:32]
        self.R=self.Text_bin[32:64]
        self.RofRounds.append((self.R))
        self.LofRounds.append((self.L))
    def XOR(self,X,Y):
        text_ip=""
        for i in range(len(X)):
           if X[i] =='1' and Y[i] =='1':
               text_ip=text_ip+'0'
           if X[i] =='1' and Y[i] =='0':
               text_ip=text_ip+'1'
           if X[i] =='0' and Y[i] =='1':
               text_ip=text_ip+'1'
           if X[i] =='0' and Y[i] =='0':
               text_ip=text_ip+'0'
        return text_ip
    def selection_table(self,Rselect):
        text_ip=""
        for i in range (self.object.select.__len__()):
            text_ip=text_ip+Rselect[self.object.select[i]-1]
        return text_ip


    def initkey(self):
        self.object1.keytoPin()
        self.object1.KEyPC1()
        self.Keys=self.object1.rounds()

    def final_ip(self):
        self.finalRandL=self.R+self.L
        text_ip=""
        for i in range(len(self.finalRandL)):
            text_ip=text_ip+self.finalRandL[self.object.final_ip[i]-1]
        return(text_ip)
    def finato(self,text):
        textcie=""
        temp=""
        for i in range(len(text)):
            if(i%4==3):
                temp=temp+text[i]
                textcie=textcie+self.object.binarary27ex(temp)
                temp=""
            else:
                temp=temp+text[i]

        return textcie















