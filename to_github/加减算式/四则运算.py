import random
#+=1,-=2,X=3,/=4
t = 0
def AA():
    a = random.randint(2, 9)
    b = random.randint(2, 9)    
    F1 = random.randint(1, 2)
    if F1==1:
        c = random.randint(2, 99)
        #print(str(a)+"×"+str(b)+"＋"+str(c)+"＝"+ str(a*b+c))
        ss = str(a)+"×"+str(b) + "＋" + str(c) + "＝" + "___"
        return(ss,str(a*b+c))
    else:
        c = random.randint(2, a*b-1)
        #print(str(a)+"×"+str(b)+"－"+str(c)+"＝"+str(a*b-c))
        ss = str(a)+"×"+str(b) + "－" + str(c) + "＝" + "___"
        return(ss,str(a*b-c))
        
    
 
def BB():    
    a = random.randint(2, 9)
    b = random.randint(2, 9)    
    F1 = random.randint(1, 2)
    if F1==1:
        c = random.randint(2, 99)        
        #print(str(a*b)+"÷"+str(a)+"＋"+str(c)+"＝"+str(b+c))
        ss = str(a*b)+"÷"+str(a)+"＋"+str(c)+"＝" + "___"
        return(ss,str(b+c))
    else:
        c = random.randint(1, b-1)
        #print(str(a*b)+"÷"+str(a)+"－"+str(c)+"＝"+str(b-c))
        ss = str(a*b)+"÷"+str(a)+"－"+str(c)+"＝" + "___"
        return(ss,str(b-c))


def CC():    
    a = random.randint(2, 9)
    b = random.randint(2, 9)    
    F1 = random.randint(1, 2)
    if F1==1:
        c = random.randint(2, 99)
        #print(str(c) + "＋" + str(a)+"×"+str(b) + "＝" + str(a*b+c))
        ss = str(c) + "＋" + str(a)+"×"+str(b) + "＝" + "___"
        return(ss,str(c+a*b))  
    else:
        c = random.randint(a*b, 99)
        #print(str(c) + "－" + str(a)+"×"+str(b)+"＝"+str(c-a*b))
        ss = str(c) + "－" + str(a) + "×" + str(b) + "＝" + "___"
        return(ss,str(c-a*b)) 
     
        
        
def DD():
    a = random.randint(2, 9)
    b = random.randint(2, 9)    
    F1 = random.randint(1, 2)
    if F1==1:
        c = random.randint(2, 99)        
        #print(str(c) + "＋" + str(a*b) + "÷" + str(a) +  "＝" + str(b+c))
        ss = str(c) + "＋" + str(a*b) + "÷" + str(a) +  "＝" + "___"
        return(ss,str(b+c))
    else:
        c = random.randint(b, 99)
        #print(str(c) + "－" + str(a*b)+"÷"+str(a) + "＝" + str(c-b))
        ss = str(c) + "－" + str(a*b)+"÷"+str(a) + "＝" + "___"
        return(ss,str(c-b))
w1 = []
w2 = []

for i in range(100):
    s = random.randint(1, 4)
    if s == 1:
        e = AA()        
    if s == 2:
        e = BB()
    if s == 3:
        e = CC()
    if s == 4:
        e = DD()
    w1.append(e[0])
    w2.append(e[1])
y = 1    
for i in range(len(w1)):
    kongbai = 15 - len(w1[i]) -len(str(y))
    for k in range(kongbai) :
        w1[i] = w1[i] + " "
    w1[i] = "(" + str(y) + ")" + "、" + w1[i]
    y = y + 1
    
y = 1      
for i in w1:    
    if y % 1 == 0:
        print(i)
    else:
        print(i,end = "")
    y = y + 1

 
    
        
y = 1    
for i in range(len(w2)):
    kongbai = 7 - len(w2[i]) -len(str(y))
    for k in range(kongbai) :
        w2[i] = w2[i] + " "
    w2[i] = "("+str(y) + ")" + "、" + w2[i]
    y = y + 1
    
    
y = 1      
for i in w2:    
    if y % 100 == 0:
        print(i)
    else:
        print(i,end = "")
    y = y + 1        
a1 = ""
y = 1
for i in range(len(w1)):
    if y % 3 == 0:
        a1 = a1 + w1[i]+"\n"
    else:
        a1 = a1 + w1[i]
    y = y + 1
print(a1)


  
  
        
    
    
   