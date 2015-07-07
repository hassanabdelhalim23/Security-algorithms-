from fractions import gcd
#Cesar y=text, Ke=KEy
def cesar(y,ke):
    x=y
    txt=""
    key=ke
    for object in x:

        cr=ord(object)
        if cr==32:
            cr=0
        else:
            cr=cr-96
        z=(cr+key)%27
        if z==0:
           txt=txt+chr(32)
        else:
             txt=txt+chr(z+96)

    return txt
#Cesar y=text, Ke=KEy
def cesar_rev(y,ke):
    x=y
    txt=""
    key=ke
    for object in x:
        cr=ord(object)
        if cr==32:
            cr=0
        else:
            cr=cr-96
        z=(cr-key)%27
        if z==0:
           txt=txt+chr(32)
        else:
            if z<0:
                z=z+27
            txt=txt+chr(z+96)
    return txt
def Simple_shift(y,ke):
    x=y
    key=ke
    txt=""
    for object in range(len(x)):
         cr=ord(x[object])
         index=object%len(key)
         cr1=ord(key[index])
         if cr==32:
             cr=0
         else:
             cr=cr-96
         if cr1==32:
             cr1=0
         else:
             cr1=cr1-96
         z=(cr+cr1)%27
         if z==0:
             txt=txt+chr(32)
         else:
             txt=txt+chr(z+96)
    return txt
def Full_vigener(y,ke):
    x=y.replace(" ","")
    key=ke
    txt=""
    for object in range(len(x)):
         cr=ord(x[object])
         index=object%len(key)
         cr1=ord(key[index])
         cr=cr-97
         cr1=cr1-97
         z=(cr+cr1)%26
         txt=txt+chr(z+97)
    return txt
def FullVigener_rev(y,ke):
    x=y.replace(" ","")
    key=ke
    txt=""
    for object in range(len(x)):
         cr=ord(x[object])
         index=object%len(key)
         cr1=ord(key[index])
         cr=cr-97
         cr1=cr1-97
         z=(cr-cr1)%26
         if z<0:
             z=z+26
         txt=txt+chr(z+97)
    return txt
def SimpleShift_rev(y,ke):
    x=y
    key=ke
    txt=""
    for object in range(len(x)):
         cr=ord(x[object])
         index=object%len(key)
         cr1=ord(key[index])
         if cr==32:
             cr=0
         else:
             cr=cr-96
         if cr1==32:
             cr1=0
         else:
             cr1=cr1-96
         z=(cr-cr1)%27
         if z==0:
             txt=txt+chr(32)
         else:
              if z<0:
                z=z+27
              txt=txt+chr(z+96)
    return txt
#Transportion Y= TEXT and Key=ke
def transportaion(y,ke):
     x=y.replace(" ","")
     sec=""
     key=ke
     object=[]
     txt=""
     index=0
     test=len(x)-1
     for cr in range(len(x)):
         if (cr%len(key))==(len(key)-1):
             txt=txt+x[cr]
             object.append(txt)
             txt=""
         else:
             txt=txt+x[cr]
     while(test%len(key))!=(len(key)-1):
          txt=txt+chr(index+97)
          test=test+1
          index=index+1
     if len(txt)!=0:
        object.append(txt)
     while min(key)!='{':
         index1=key.index(min(key))
         key=key.replace(min(key),'{')
         for ce in object:
             sec=sec+ce[index1]
     return sec
#Transportion Y= TEXT and Key=ke
def transportation_rev(y,ke):
    x=y.replace(" ","")
    key=ke
    ke=sorted(key)
    txt=""
    txt1=""
    for ob in ke:
      txt=txt+ob
      len1=int(len(x)/len(key))
    for index in range(int(len(x)/len(key))):
          for index1 in range(len(key)):
              z=txt.index(key[index1])
              txt1=txt1+(x[((z*len1)+index)])
    return txt1
#AFFine Y= TEXT and Key=key and p =m
def affine(y,p,key):
    txt=""
    plain=y.replace(" ","")
    var=gcd(p,26)
    if var==1:
       for x in plain:
         cr=ord(x)
         cr=cr-97
         z=(p*cr+key)%26
         txt=txt+chr(z+97)
       return  txt
    else:
       return "No Cant do it"
#AFFine Y= TEXT and Key=key and p =m
def affine_rev(y,p,key):
    txt=""
    plain=y.replace(" ","")
    n=p
    object=[]
    m=26
    y1=1
    x1=0
    while True:
        z=int(m/n)
        object.append(z)
        temp=m%n
        m=n
        n=temp
        if temp==0:
            break
    object.reverse()
    for index in range(1,len(object)):
        temp=y1
        y1=(y1*object[index])+x1
        x1=temp
    if(y1*p)>(x1*26):
        m1=y1
    else:
        m1=26-y1
    print("mod Inverse"+str(m1))
    for index1 in plain:
        cr=ord(index1)
        cr=cr-97
        z=(m1*(cr-key))%26
        while z<0:
            z=z+26
        txt=txt+chr(z+97)
    return txt
#PlayFair text=txt and key=key
def playfair(txt,key):
    txt = txt.replace(" ", "")
    key = key.replace(" ", "")
    txtcie=""
    txt=txt.replace(" ","")
    txt1=""
    index=0
    for x in key:
        test=txt1.find(x)
        if test==-1:
            if not(((x=='i')and(txt1.find('j')!=-1))or(x=='j')and(txt1.find('i')!=-1)):
               txt1=txt1+x
               index=index+1

    if index!=25:
        for car in range(26):
             test=txt1.find(chr(car+97))
             if(test==-1):
               if not(((chr(car+97)=='i')and(txt1.find('j')!=-1))or(chr(car+97)=='j')and(txt1.find('i')!=-1)):
                 txt1=txt1+chr(car+97)
                 index=index+1
             if index==25:
                 break
    point=0
    print("Data to select it "+txt1)
    if(txt1.find('j')!=-1):
        txt=txt.replace('i','j')
    else:
        txt=txt.replace('j','i')
    while point <len(txt)-1:
        if(txt[point]!=txt[point+1]):
            x=int(txt1.find(txt[point])/5)
            y=txt1.find(txt[point])%5
            x1=int(txt1.find(txt[point+1])/5)
            y1=txt1.find(txt[point+1])%5
            if x==x1:
                y=y+1
                y=y%5
                y1=y1+1
                y1=y1%5
            if(y==y1):
                x=x+1
                x=x%5
                x1=x1+1
                x1=x1%5
            if(x!=x1)and(y1!=y):
                temp=y1
                y1=y
                y=temp
            txtcie=txtcie+txt1[x*5+y]+txt1[x1*5+y1]
            point=point+2
        elif(txt[point]==txt[point+1]):
            x=int(txt1.find(txt[point])/5)
            y=txt1.find(txt[point])%5
            x1=int(txt1.find('x')/5)
            y1=txt1.find('x')%5
            if x==x1:
                y=y+1
                y=y%5
                y1=y1+1
                y1=y1%5
            if(y==y1):
                x=x+1
                x=x%5
                x1=x1+1
                x1=x1%5
            if(x!=x1)and(y1!=y):
                temp=y1
                y1=y
                y=temp
            txtcie=txtcie+txt1[x*5+y]+txt1[x1*5+y1]
            point=point+1
    if point <len(txt):
       x=int(txt1.find(txt[point])/5)
       y=txt1.find(txt[point])%5
       x1=int(txt1.find('x')/5)
       y1=txt1.find('x')%5
       if x==x1:
          y=y+1
          y=y%5
          y1=y1+1
          y1=y1%5
       if(y==y1):
          x=x+1
          x=x%5
          x1=x1+1
          x1=x1%5
       if(x!=x1)and(y1!=y):
          temp=y1
          y1=y
          y=temp
       txtcie=txtcie+txt1[x*5+y]+txt1[x1*5+y1]
    return txtcie
# Playfair
def playfair_rev(txt,key):
    txt = txt.replace(" ", "")
    key = key.replace(" ", "")
    txtcie=""
    txt=txt.replace(" ","")
    txt1=""
    index=0
    for x in key:
        test=txt1.find(x)
        if test==-1:
            if not(((x=='i')and(txt1.find('j')!=-1))or(x=='j')and(txt1.find('i')!=-1)):
              txt1=txt1+x
              index=index+1
    if index!=25:
        for car in range(26):
             test=txt1.find(chr(car+97))
             if(test==-1):
               if not(((chr(car+97)=='i')and(txt1.find('j')!=-1))or(chr(car+97)=='j')and(txt1.find('i')!=-1)):
                    txt1=txt1+chr(car+97)
                    index=index+1
             if index==25:
                 break
    point=0
    print("Data to select it "+txt1)
    if(txt1.find('j')!=-1):
        txt=txt.replace('i','j')
    else:
        txt=txt.replace('j','i')
    while point <len(txt)-1:
        if(txt[point]!=txt[point+1]):
            x=int(txt1.find(txt[point])/5)
            y=txt1.find(txt[point])%5
            x1=int(txt1.find(txt[point+1])/5)
            y1=txt1.find(txt[point+1])%5
            if x==x1:
                y=y-1
                if y<0:
                    y=y+5
                y1=y1-1
                if y1<0:
                   y1=y1+5
            if(y==y1):
                x=x-1
                if x<0:
                    x=x+5
                x1=x1-1
                if x1<0:
                    x1=x1+5
            if(x!=x1)and(y1!=y):
                temp=y1
                y1=y
                y=temp
            txtcie=txtcie+txt1[x*5+y]+txt1[x1*5+y1]
            point=point+2
        elif(txt[point]==txt[point+1]):
             x=int(txt1.find(txt[point])/5)
             y=txt1.find(txt[point])%5
             x1=int(txt1.find('x')/5)
             y1=txt1.find('x')%5
             if x==x1:
                y=y-1
                if y<0:
                    y=y+5
                y1=y1-1
                if y1<0:
                   y1=y1+5
             if(y==y1):
                x=x-1
                if x<0:
                    x=x+5
                x1=x1-1
                if(x1 <0):
                    x1=x1+5
             if(x!=x1)and(y1!=y):
                temp=y1
                y1=y
                y=temp
             txtcie=txtcie+txt1[x*5+y]+txt1[x1*5+y1]

             point=point+1
    if point <len(txt):
       x=int(txt1.find(txt[point])/5)
       y=txt1.find(txt[point])%5
       x1=int(txt1.find('x')/5)
       y1=txt1.find('x')%5
       if x==x1:
          y=y-1
          if(y<0):
              y=y+5
          y1=y1-1
          if(y1<0):
              y1=y1+5
       if(y==y1):
          x=x-1
          if(x<0):
              x=x+1
          x1=x1-1
          if(x1<0):
              x1=x1+5
       if(x!=x1)and(y1!=y):
          temp=y1
          y1=y
          y=temp
       txtcie=txtcie+txt1[x*5+y]+txt1[x1*5+y1]

    return txtcie
#Commbination of transportion and subtition
def comandofSubandtrans(plain):
    plain = plain.replace(" ", "")
    txt=""
    txtcie=""
    for index in plain:
        cr=ord(index)
        cr=cr-97
        w=int(cr/5)
        z=cr%5
        if(w==5)and(z==0):
            txt=txt+"db"
        else:
            txt=txt+chr(w+97)
            txt=txt+chr(z+97)
    txt1=txt[0:int(len(txt)/2)]
    txt2=txt[int(len(txt)/2):]
    print("First Sentence "+txt1)
    print("Second Sentence "+txt2)
    for index1 in range(len(txt1)):
        cr=ord(txt1[index1])-97
        cr1=ord(txt2[index1])-97
        txtcie=txtcie+chr((cr*5+cr1)+97)
    return txtcie
def comandofSubandtrans_rev(plain):
    plain = plain.replace(" ", "")
    txt1=""
    txt2=""
    txtcie=""
    for index in plain:
        cr=ord(index)
        cr=cr-97
        w=int(cr/5)
        z=cr%5
        if(w==5)and(z==0):
            txt1=txt1+"d"
            txt2=txt2+"b"
        else:
            txt1=txt1+chr(w+97)
            txt2=txt2+chr(z+97)
    tx=""
    t1=""
    print("first sentence "+txt1)
    print("second sentence "+txt2)
    txt1=txt1+txt2
    for index1 in range(len(txt1)):
        if index1%2==0 and index1!=0:
            t1=t1+chr(((ord(tx[0])-97)*5+ord(tx[1])-97)+97)
            tx=""
            tx=tx+txt1[index1]
        else:
            tx=tx+txt1[index1]
    if len(txt1)-1%2!=0:
         t1=t1+chr(((ord(tx[0])-97)*5+ord(tx[1])-97)+97)

    txtcie=t1
    return txtcie


