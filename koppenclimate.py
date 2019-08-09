# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:35:09 2015

@author: MR
"""

#input values
a=input('Mean January max (in dC): ')
b=input('Mean February max: ')
c=input('Mean March max: ')
d=input('Mean April max: ')
e=input('Mean May max: ')
f=input('Mean June max: ')
g=input('Mean July max: ')
h=input('Mean August max: ')
i=input('Mean September max: ')
j=input('Mean October max: ')
k=input('Mean November max: ')
l=input('Mean December max: ')

m=input('Mean January min: ')
n=input('Mean February min: ')
o=input('Mean March min: ')
p=input('Mean April min: ')
q=input('Mean May min: ')
r=input('Mean June min: ')
s=input('Mean July min: ')
t=input('Mean August min: ')
u=input('Mean September min: ')
v=input('Mean October min: ')
w=input('Mean November min: ')
x=input('Mean December min: ')

aa=input('January precipitation (in mm): ')
bb=input('February precipitation: ')
cc=input('March precipitation: ')
dd=input('April precipitation: ')
ee=input('May precipitation: ')
ff=input('June precipitation: ')
gg=input('July precipitation: ')
hh=input('August precipitation: ')
ii=input('September precipitation: ')
jj=input('October precipitation: ')
kk=input('November precipitation: ')
ll=input('December precipitation: ')

alt=input('Height above sea level (nearest m): ') #for altitude correction
deltaT=int(alt)/1000.0*6.4
nors=input('Northern or Southern hemisphere location (N=0, S=1): ')
nors=int(nors)

y=[float(a),float(b),float(c),float(d),float(e),float(f),float(g),float(h),float(i),float(j),float(k),float(l)] #temp max
z=[float(m),float(n),float(o),float(p),float(q),float(r),float(s),float(t),float(u),float(v),float(w),float(x)] #temp min
yy=[float(aa),float(bb),float(cc),float(dd),float(ee),float(ff),float(gg),float(hh),float(ii),float(jj),float(kk),float(ll)] #rainfall

A=0
B=0
C=0
D=0
E=0
Af=0
Am=0
Aw=0
As=0
BW=0
BS=0
Bh=0
Bk=0
Bhw=0
Bhs=0
Bhf=0
Bnc=0
Bkw=0
Bks=0
Bkf=0
Cf=0
Cw=0
Cs=0
Da=0
Db=0
Dc=0
Dd=0
ET=0
EF=0
Ef=0
Ew=0
Es=0
Enc=0

#averages
zz=0
avtmx=0 #average max temp
while zz<11.1:
    avtmx=avtmx+y[zz]
    zz=zz+1
avtmx=avtmx/12.0
aaa=0
avtmn=0 #average min temp
while aaa<11.1:
    avtmn=avtmn+z[aaa]
    aaa=aaa+1
avtmn=avtmn/12.0
bbb=0
avr=0 #average rainfall
while bbb<11.1:
    avr=avr+yy[bbb]
    bbb=bbb+1
avr=avr/12.0
avt=(avtmx+avtmn)/2.0 #average temp
avmt=[(y[0]+z[0])/2.0,(y[1]+z[1])/2.0,(y[2]+z[2])/2.0,(y[3]+z[3])/2.0,(y[4]+z[4])/2.0,(y[5]+z[5])/2.0,(y[6]+z[6])/2.0,(y[7]+z[7])/2.0,(y[8]+z[8])/2.0,(y[9]+z[9])/2.0,(y[10]+z[10])/2.0,(y[11]+z[11])/2.0] #average monthly temp
mnr=min(yy) #min rainfall
mxr=max(yy) #max rainfall
totr=sum(yy) #total rainfall
mnavt=min(avmt) #min average monthly temperature
mxavt=max(avmt) #max average monthly temperature
mon=100-totr/25.0 #monsoon
sh=yy[3]+yy[4]+yy[5]+yy[6]+yy[7]+yy[8] #sun high rain
sl=yy[0]+yy[1]+yy[2]+yy[9]+yy[10]+yy[11] #sun low rain
shr=[yy[3],yy[4],yy[5],yy[6],yy[7],yy[8]] #sun high / summer
slr=[yy[0],yy[1],yy[2],yy[9],yy[10],yy[11]] #sun low / winter
if nors==1: #north/south swap
    tt=sh
    sh=sl
    sl=tt
    tt=0
    ttt=shr
    shr=slr
    slr=ttt
    ttt=0
else: 
    tt=0
    ttt=0
if mnr==min(shr):
    s=1
elif mnr==min(slr):
    w=1
else:
    w=0
    s=0
mn10=[] #inital for months of 10dC or more
for ab in avmt:
    if ab>=10:
        mn10.append(ab)
mn10n=int(len(mn10))
mxsr=max(shr)
mxwr=max(slr)
mnsr=min(shr)
mnwr=min(slr)
mr60=0
for x in yy:
    if x<60:
        mr60=mr60+1
    else: mr60=mr60
#potential evapourtraspiration test
print('')
etf=0 #evapourtraspiration factor
rf=sh/totr #sun high rain fraction
if rf>=0.7:
    etf=280
elif rf>30 and rf<70:
    etf=140
elif rf<=30:
    etf=0
else: print('er1')
pet=20*avt+etf
print('Potential evapouration:',pet,'mm')
print('Actual precipitation:',totr,'mm')
if totr<(0.5*pet): #desert
    BW=1
    print('Desert test passed: precipitation is less than 1/2 the potential evapouration')
    B=1
elif totr>=(0.5*pet) and totr<pet: #steppe
    BS=1
    print('Steppe test passed: precipitation is less than the potential evapouration, but more than 1/2 the potential evapouration')
    B=1
else:
    BW=0
    BS=0
#temperature test
if BW==0 and BS==0:
    if mnavt>=18:
        A=1
        print('Tropical temperature test passed: min monthley average temperature',mnavt,'dC is greater or equal to 18 dC')
    elif mxavt<10:
        E=1
        print('Polar temperature test passed: max monthley average temperature',mxavt,'dC is less than 10 dC')
    elif mxavt>=10 and mnavt<18:
        print('Temperate temperature test passed: min monthley average temperature',mnavt,'dC is less than 18 dC and the max average temperature',mxavt,'dC is greater than or equal to 10 dC')
        if mnavt>-3: #can be 0dC
            C=1
            print('Coastal temperature test passed: min monthley average temperature',mnavt,'dC is greater than -3 dC')
        elif mnavt<=-3: #can be 0dC
            D=1
            print('Continential temperature test passed: min monthley average temperature',mnavt,'dC is less than or equal to -3 dC')
        else: print('er2')
    else: print('er3')
#temperature heat test
if A==1:
    A=1
elif B==1:
    if avt<18: #can be 0dC
        Bk=1
        print('Cold arid test passed: average temperature',avt,'dC is less than 18 dC')
    else: 
        Bh=1
        print('Hot arid test passed: average temperature',avt,'dC is greater or equal to 18 dC')
elif C==1 or D==1:
    if mxavt>=22 and mn10n>3:
        Da=1
        print('Sub tropical degree of heat test passed: max average temperature',mxavt,'dC is greater than or equal to 22 dC and',mn10n,'months are greater than the 10 dC average monthly and greater than or equal to the 4 months required')
    elif mxavt<22 and mn10n>3:
        Db=1
        print('Warm degree of heat test passed: max monthley average temperature',mxavt,'dC is less than 22 dC and',mn10n,'months are greater than the 10 dC average monthly temperature and greater than or equal to the 4 months required')
    elif mn10n<4:
        Dc=1
        print('Cold degree of heat test passed: max monthley average temperature',mxavt,'dC is less than 22 dC and',mn10n,'months are greater than the 10 dC average monthly temperature and less than or equal to the 3 months required')
    else: print('er4')
    if mnavt<-38:
        Dd=1
        Da=0
        Db=0
        Dc=0
        print('Extreme cold degree of heat passed: min monthley average temperature',mnavt,'dC is less than -38 dC')
elif E==1:
    if mxavt>0:
        ET=1
        print('Polar tundra test passed: max monthley average temperature',mxavt,'dC is greater than 0 dC')
    elif mxavt<=0:
        EF=1
        print('Polar ice cap test passed: max monthley average temperature',mxavt,'dC is less than or equal to 0 dC')
    else: print('er5')
#rainfall test
if A==1:
    if mnr>=60:
        Af=1
        print('Even and required precipitation test passed: greater than of equal to 60 mm of rain a month, with the min monthly rainfall of',mnr,'mm')
    elif mnr<60 and mnr>=mon:
        Am=1
        print('Monsoonal precipitation test passed: there are',mnr,'mm with precipitation less than 60 mm and the min monthley rainfall of',mnr,'mm that is greater than or equal to the',mon,'mm monsonal limit')
    elif mnr<60 and mnr<mon:
        if w==1:
            Aw=1
            print('Wet + dry precipitation test passed: there are',mr60,'month  with precipitation less than 60 mm and the min monthley rainfall of',mnr,'mm that is less than the',mon,'mm monsonal limit')
            print('Winter dry peciputation test passed: winter precipitation of',sl,'mm is less than summer precipitation of',sh,'mm, with',rf*100,'% of the precipitation in the summer')            
        elif s==1:
            As=1
            print('Wet + dry precipitation test passed: there are',mr60,'month with precipitation less than 60 mm and the min monthley rainfall of',mnr,'mm that is less than the',mon,'mm monsonal limit')
            print('Summer dry peciputation test passed: winter precipitation of',sl,'mm is greater than summer precipitation of',sh,'mm, with',rf*100,'% of the precipitation in the summer')            
        else: print('er6')
    else: print('er7')
elif B==1:
    if Bh==1: #pos modification
        if mxr>=60 and rf>=0.7:
            Bhw=1
            print('Winter dry pecipitation test passed: winter precipitation of',sl,'mm is less than summer precipitation of',sh,'mm, with',rf*100,'% of the precipitation in the summer and the max precipitation of',mxr,'mm is greater than 60 mm and rain fraction greater than or equal to 70%')            
        elif mxr>=60 and rf<=0.3:
            Bhs=1
            print('Summer dry pecipitation test passed: winter precipitation of',sl,'mm is greater than summer precipitation of',sh,'mm, with',rf*100,'% of the precipitation in the summer and the max precipitation of',mxr,'mm is greater than 60 mm and rain fraction less than or equal to 30%')            
        elif mxr>=60:
            Bhf=1
            print('Even and required precipitation test passed: there was',rf*100,'% of the precipitation in the summer, which is between the 30-70% required and the max precipitation of',mxr,'mm is greater than 60 mm')
        else: 
            Bnc=1
            print('Precipitation test failed: the max rainfall',mxr,'is less than 60 mm')
    elif Bk==1: #pos mod
        if mxr>=30 and rf>=0.7:
            Bkw=1
            print('Winter dry pecipitation test passed: winter precipitation of',sl,'mm is less than summer precipitation of',sh,'mm, with',rf*100,'% of the precipitation in the summer and the max precipitation of',mxr,'mm is greater than 30 mm and rain fraction greater than or equal to 70%')            
        elif mxr>=30 and rf<=0.3:
            Bks=1
            print('Summer dry pecipitation test passed: winter precipitation of',sl,'mm is greater than summer precipitation of',sh,'mm, with',rf*100,'% of the precipitation in the summer and the max precipitation of',mxr,'mm is greater than 30 mm and rain fraction less than or equal to 30%')            
        elif mxr>=30:
            Bkf=1
            print('Even and required precipitation test passed: there was',rf*100,'% of the precipitation in the summer, which is between the 30-70% required and the max precipitation of',mxr,'mm is greater than 30 mm')
        else: 
            Bnc=1
            print('Precipitation test failed: the max precipitation',mxr,'mm is less than 30 mm')
elif C==1 or D==1:
    if s==1 and mnsr<1/3.0*mxwr and mnsr<30: #30mm min
        Cs=1
        print('Summer dry pecipitation test passed: the driest summer precipitation of',mnsr,'mm is less than x1/3 the wettest winter precipitation of',mxwr,'mm, with',rf*100,'% of the precipitation in the summer and the min summer precipitation of',mnsr,'mm is less than 30 mm')            
    elif w==1 and mnwr<1/10.0*mxsr and mnwr<30: #30mm min
        Cw=1
        print('Winter dry pecipitation test passed: the driest winter precipitation of',mnwr,'mm is x1/10 less than the wettest summer precipitation of',mxsr,'mm, with',rf*100,'% of the precipitation in the summer and the min winter precipitation of',mnwr,'mm is less than 30 mm')            
    else: 
        Cf=1 #la print- pos swap 2nd part + 30mm lim- done
        print('Even precipitation test passed: the driest winter precipitation of',mnwr,'mm is not less than the wettest summer precipitation threshold of',1/10*mxsr,'mm and the driest summer precipitation of',mnsr,'mm is not less than the westtest winter precipitation threshold of',1/3*mxwr,'mm or all months rainfall are greater than 30 mm')
elif E==1:
    if mxr>=30:
        if s==1 and mnsr<1/3.0*mxwr: #30mm min
            Es=1
            print('Summer dry pecipitation test passed: the driest summer precipitation of',mnsr,'mm is less than x1/3 the wettest winter precipitation of',mxwr,'mm, with',rf*100,'% of the precipitation in the summer and the min summer precipitation of',mnsr,'mm is less than 30 mm')            
        elif w==1 and mnwr<1/10.0*mxsr:
            Ew=1
            print('Winter dry pecipitation test passed: the driest winter precipitation of',mnwr,'mm is x1/10 less than the wettest summer precipitation of',mxsr,'mm, with',rf*100,'% of the precipitation in the summer and the min winter precipitation of',mnwr,'mm is less than 30 mm')            
        else: 
            Ef=1
            print('Even precipitation test passed: the driest winter precipitation of',mnwr,'mm is not less than the wettest summer precipitation threshold of',1/10*mxsr,'mm and the driest summer precipitation of',mnsr,'mm is not less than the westtest winter precipitation threshold of',1/3*mxwr,'mm or all months rainfall are greater than 30 mm')
    else: 
        Enc=1
        print('Precipitation test failed: the max precipitation',mxr,'mm is less than 30 mm')
else: print('er8')
#classification
v1=[A*1,B*2,C*3,D*4,E*5]
vA=[Af*1,Am*2,Aw*3,As*4]
vB=[BW*1,BS*2]
vB2=[Bh*1,Bk*2]
vB3=[Bhw*1,Bhs*2,Bhf*3,Bnc*4,Bkw*5,Bks*6,Bkf*7]
vC=[Cf*1,Cw*2,Cs*3]
vD=[Da*1,Db*2,Dc*3,Dd*4]
vE=[ET*1,EF*2]
vE2=[Ef*1,Ew*2,Es*3,Enc*4]
v1dic={1:'A',2:'B',3:'C',4:'D',5:'E'}
vAdic={1:'f',2:'m',3:'w',4:'s'}
vBdic={1:'W',2:'S'}
vB2dic={1:'h',2:'k'}
vB3dic={1:'w',2:'s',3:'f',4:'n',5:'w',6:'s',7:'f'}
vCdic={1:'f',2:'w',3:'s'}
vDdic={1:'a',2:'b',3:'c',4:'d'}
vEdic={1:'T',2:'F'}
vE2dic={1:'f',2:'w',3:'s',4:'n'}
#classification combo
combo=0
if max(v1)==1:
    combo=[v1dic[max(v1)],vAdic[max(vA)]]
    ct=combo[0]+combo[1]
elif max(v1)==2:
    combo=[v1dic[max(v1)],vBdic[max(vB)],vB2dic[max(vB2)],vB3dic[max(vB3)]]
    ct=combo[0]+combo[1]+combo[2]+combo[3]
elif max(v1)==3 or max(v1)==4:
    combo=[v1dic[max(v1)],vCdic[max(vC)],vDdic[max(vD)]]
    ct=combo[0]+combo[1]+combo[2]
elif max(v1)==5:
    combo=[v1dic[max(v1)],vEdic[max(vE)],vE2dic[max(vE2)]]
    ct=combo[0]+combo[1]+combo[2]
else: print('er: no class')
#plot
import matplotlib.pyplot as plt
fig=plt.figure()
fig.set_size_inches(12,12)
xaxis2=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
xaxis=[1,2,3,4,5,6,7,8,9,10,11,12]
ax=plt.subplot()
ax2=ax.twinx()
ax2.plot(xaxis,y,'r',label='max temp dC',linewidth=2.0) and ax2.plot(xaxis,z,'b',label='min temp dC',linewidth=2.0) and ax2.plot(xaxis,avmt,'g',label='average temp dC',linewidth=2.0)
ax.bar(xaxis,yy,color=[0,0.5,1],label='rainfall',align='center')
ax2.legend(loc=1)
ax.legend(loc=2)
plt.title(ct)
ax.set_xlabel('Month')
ax.set_ylabel('Rainfall mm')
plt.xticks(xaxis,xaxis2)
plt.grid(True)
ax.grid(True)
ax2.set_ylabel('Temperature dC')
max1=round(max(yy),-1)+10
max2=round(max(y),0)+5
wl1=0
wl2=round(min(z)-5,-1)
ts1=[]
ts2=[]
while wl1<=max1:
 ts1.append(wl1)
 wl1=wl1+10
while wl2<=max2:
    ts2.append(wl2)
    wl2=wl2+5
ax.yaxis.set_ticks(ts1)
ax2.yaxis.set_ticks(ts2)
#sort size and lgend alignment loc
plt.show()
print('\n Climate type:',ct,'\n')

#import matplotlib.pyplot as plt 
#ax = plt.gca()
#ax2 = ax.twinx()
#plt.axis('normal')
#ax2.axvspan(74, 76, facecolor='g', alpha=1)
#ax.plot(range(50), 'b',linewidth=1.5)
#ax.set_ylabel("name",fontsize=14,color='blue')
#ax2.set_ylabel("name2",fontsize=14,color='blue')
#ax.set_ylim(ymax=100)
#ax.set_xlim(xmax=100)
#ax.grid(True)
#plt.title("name", fontsize=20,color='black')
#ax.set_xlabel('xlabel', fontsize=14, color='b')
#plt.show()

#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib import rc
#rc('mathtext', default='regular')

#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(time, Swdown, '-', label = 'Swdown')
#ax.plot(time, Rn, '-', label = 'Rn')
#ax2 = ax.twinx()
#ax2.plot(time, temp, '-r', label = 'temp')
#ax.legend(loc=0)
#ax.grid()
#ax.set_xlabel("Time (h)")
#ax.set_ylabel(r"Radiation ($MJ\,m^{-2}\,d^{-1}$)")
#ax2.set_ylabel(r"Temperature ($^\circ$C)")
#ax2.set_ylim(0, 35)
#ax.set_ylim(-20,100)
#plt.show()

#A: >=18dC, f: >=60mm each month, m: 1 month <60mm and >100-tot/25, w/s: 1 month <60mm and <100-tot/25 (summer is apr-sep, winter is oct-mar)
#B: 20*average_temperature+(280 for >0.7 rain in summer, 140 for 0.3-0.7, 0 for <0.3 rain in summer), BW: rain<0.5,BS: [<]1-0.5, h: avT>=18dC or clodest month >0dC, k: avT<18dC or coldest month <=0dC, w/s: >60mm for >=18dC, >30mm for <18dC and 0.7 rain in that 1/2 of year
#C: avT >10dC in summer, coldest month >=-3dC or >0dC, w: driest month < 1/10 wettest summer month (and <30mm), s: driest month < 1/3 wettest month (and <30mm), f: neither, a: warmest month >=22dC, b: warmest month <22dC + 4 months >10dC, c: <4 month >10dC (la)
#D: avT >10dC in summer, coldest month <-3dC or <=0dC, others same, d: <4 months >10dC + coldest month <-38dC
#E: all months <=10dC, T:warmest month 0-10dC, F: all months <0dC, w/s/f >30mm in wettest + C/D useage