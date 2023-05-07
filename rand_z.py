import random
import math

def generate(i1,i2):
    k=[]
    for i in range(i2):
        if i1==6:
            k.append(drob())
        if i1==8:
            k.append(step())
        if i1==9:
            k.append(urov())
        if i1==10:
            k.append(vars())
    return k
        
    
def drob():
    i=random.randint(2,5)
    k=[]
    w='Решить уравнение:'
    m=0
    for o in range(i):
        k.append([random.randint(-50,50),random.randint(1,10),random.randint(1,5)])
    for i in k:
        w=w+'('+str(i[0])+'*'+str(i[1])+'^'+str(i[2])+')'
        m=m+(i[0]*(i[1]**i[2]))
    w=w+"\n"+'Ответ:'+str(m)
    return w

def step():
    i=random.randint(1,2)
    if i==1:
        k=[random.randint(5,150),random.randint(5,150),random.randint(5,50),random.randint(1,2),random.randint(5,60),random.randint(5,60)]
        if k[3]==1:
            w='Решите:'+str(k[2])+'ab*('+str(k[4])+'a+'+str(k[5])+'b) a='+str(k[0])+' b='+str(k[1])
            l=k[2]*k[1]*k[0]*(k[4]*k[0]+k[5]*k[1])
        elif k[3]==2:
            w='Решите:'+str(k[2])+'ab*('+str(k[4])+'a-'+str(k[5])+'b) a='+str(k[0])+' b='+str(k[1])
            l=k[2]*k[1]*k[0]*(k[4]*k[0]-k[5]*k[1])
    else:
        k=[random.randint(2,150),random.randint(2,150),random.randint(2,80),random.randint(2,80)]
        w='Решите:(('+str(k[2])+'ab)/(a+'+str(k[2])+'b))*((a/'+str(k[3])+'b)+('+str(k[3])+'b/a)) a='+str(k[0])+' b='+str(k[1])
        l=((k[2]*k[0]*k[1])/(k[0]+k[2]*k[1]))*((k[0]/k[3]*k[1])+(k[3]*k[1]/k[0]))
    w=w+"\n"+'Ответ:'+str(l)
    return w

def urov():
    k=[0,0,0]
    while (k[0]==0):
        k=[random.randint(-40,40),random.randint(-15,15),random.randint(-40,40)]
    w='Решите квадратное уравнение: '+str(k[0])+'x^2+('+str(k[1])+')x+('+str(k[2])+')=0'
    D=k[1]**2-4*k[0]*k[2]
    if D<0:
        l='Нет решения'
    elif D==0:
        l=str((-1*k[1])/(2*k[0]))
    else:
        l=str((-1*k[1]+(math.sqrt(D)))/(2*k[0]))
        l=l+' и '+str((-1*k[1]-(math.sqrt(D)))/(2*k[0]))
    w=w+"\n"+'Решение:'+l
    return w

def vars():
    k=[random.randint(15,99)]
    k.append(random.randint(1,k[0]))
    w='В условном экперименте было '+str(k[0])+' попыток. Из них '+str(k[1])+' успешных. Какова вероятность успеха в случае выбора случайной попытки?'
    w=w+"\n"+'Ответ:'+str(k[1]/k[0])
    return w

def grafs():
    k=[random.randint(-5,5),random.randint(-10,10),random.randint(1,3)]
    if k[2]==1:
        w='График: y='+str(k[0])+'x+('+str(k[1])+')'
    elif k[2]==2:
        w='График: y='+str(k[0])+'x^2+('+str(k[1])+')'
    else:
        w='График: y='+str(k[0])+'x^3+('+str(k[1])+')'