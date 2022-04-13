# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 20:27:07 2022

@author: Asus ROG
"""

import math
import numpy

numpy.set_printoptions(3, suppress=True)

tn = int(input('Enter the total number of nodes : ')) 
te = int(input('Enter the total number of Elements : ')) 
xco = [] 
yco = [] 
for i in range(tn):
    x = float(input('Enter the x co-ordinate of node '+str(i+1)+' in mm : '))
    y = float(input('Enter the y co-ordinate of node '+str(i+1)+' in mm : '))
    xco.append(x)
    yco.append(y)
    
A = float(input('Enter the Area of cross section in mm2: '))
E = float(input('Enter the Modulous of Elasticity in N/mm2 : '))

startnode = [] 
endnode = []
memberlength = []
elcon = []
cosofel = [] 
sinofel = []

for i in range(te):  
    a = int(input('Enter the Start node of element '+str(i+1)+' : '))
    b = int(input('Enter the End node of element '+str(i+1)+' : '))
    x1 = float(xco[a-1])
    y1 = float(yco[a-1])
    x2 = float(xco[b-1])
    y2 = float(yco[b-1])
    l = math.sqrt((x2-x1)**2+(y2-y1)**2)
    con = A*E/l
    cos = (x2-x1)/l
    sin = (y2-y1)/l
    
    startnode.append(a)
    endnode.append(b)
    memberlength.append(l)
    elcon.append(con)
    cosofel.append(cos)
    sinofel.append(sin)
    
elstmat = []

for i in range(te):
    cc = float(cosofel[i])**2
    ss = float(sinofel[i])**2
    cs = float(cosofel[i])*float(sinofel[i])
    
    mat = elcon[i]*numpy.array([[cc, cs, -cc, -cs],
                               [cs, ss, -cs, -ss],
                               [-cc, -cs, cc, cs],
                               [-cs, -ss, cs, ss]])

    elstmat.append(mat)

gstmatmap = []                         
for i in range(te):                     
    m = startnode[i]*2                     
    n = endnode[i]*2                    
    add = [m-1, m, n-1, n]              
                                           
                                          
    gmat = numpy.zeros((tn*2, tn*2))    
    elmat = elstmat[i]                  
    for j in range(4):                  
        for k in range(4):              
            a = add[j]-1                
            b = add[k]-1                
            gmat[a,b] = elmat[j,k]     
    gstmatmap.append(gmat)              

GSM = numpy.zeros((tn*2, tn*2))         
for mat in gstmatmap:
    GSM = GSM+mat                      

print('\nGlobal Stiffness Matrix of the Truss\n')
print(numpy.around(GSM, 3))

displist = []
forcelist = []
for i in range(tn):
    a = str('u')+str(i+1)
    displist.append(a)
    b = str('v')+str(i+1)
    displist.append(b)
    c = str('fx')+str(i+1)
    forcelist.append(c)
    d = str('fy')+str(i+1)
    forcelist.append(d)
    
print('\n________________Support Data______________\n')

dispmat = numpy.ones((tn*2,1))
tsupn = int(input('Enter the total number of nodes having supports : ')) 
supcondition = ['P = pinned',
                'H = Horizonally restrained',
                'V = Vertically restrained ']
   
for i in range(tsupn):
    supn = int(input('\nEnter the node number of support : '))
    for a in supcondition:
        print(a)
    condition = str(input('\nEnter the condition of the support : '))
    if condition in['P', 'p']:
        dispmat[supn*2-2, 0] = 0
        dispmat[supn*2-1, 0] = 0
    elif condition in['H', 'h']:
        dispmat[supn*2-2, 0] = 0
    elif condition in['V', 'v']:
        dispmat[supn*2-1, 0] = 0
    else:
        print('Please enter valid entries')


print('\n_________________Loading____________________\n')
forcemat = numpy.zeros((tn*2,1))
tlon = int(input('Enter the total number of loaded nodes : ')) 

for i in range(tlon):
    lon = int(input('\nEnter the node number of Loading : ')) 
    fx = float(input('Enter the Horizontal load at this node in N : '))
    fy = float(input('Enter the Vertical load at this node in N : '))
    forcemat[lon*2-2, 0] = fx
    forcemat[lon*2-1, 0] = fy

rcdlist = []
for i in range(tn*2):
    if dispmat[i,0] == 0:
        rcdlist.append(i)

rrgsm = numpy.delete(GSM, rcdlist, 0)              
crgsm = numpy.delete(rrgsm, rcdlist, 1)            
rgsm = crgsm                                       
rforcemat = numpy.delete(forcemat, rcdlist, 0)    
rdispmat = numpy.delete(dispmat, rcdlist, 0)        

dispresult = numpy.matmul(numpy.linalg.inv(rgsm), rforcemat)
rin = 0
for i in range(tn*2):
    if dispmat[i,0] == 1:
        dispmat[i,0] = dispresult[rin,0]
        rin = rin+1

forceresult = numpy.matmul(GSM, dispmat)


print('\n\nGlobal Stiffness Matrix\n')
print(GSM)
print('\n\nNodes Displacement matrix of\n')
print(dispmat)
print('\n\nNodes Force matrix of\n')
print(forceresult)

newxco = []
newyco = []
count = 0
for i in range(tn):
    k = xco[i]+dispmat[count,0]
    newxco.append(k)
    count = count+1
    l = yco[i]+dispmat[count,0]
    newyco.append(l)
    count = count+1
    
newmemberlength = []
for i in range(te):
    a, b = startnode[i], endnode[i]
    x1 = float(newxco[a-1])
    y1 = float(newyco[a-1])
    x2 = float(newxco[b-1])
    y2 = float(newyco[b-1])
    l = math.sqrt((x2-x1)**2+(y2-y1)**2)
    newmemberlength.append(l)
    
numpy.set_printoptions(3, suppress=False)

elstrain = numpy.zeros((te,1))
for i in range(te):
    elstrain[i,0] = (newmemberlength[i]-memberlength[i])/(memberlength[i])

numpy.set_printoptions(3, suppress=True)

elstress = numpy.zeros((te,1))
for i in range(te):
    elstress[i,0] = E * elstrain[i,0]


elforce = numpy.zeros((te,1))
for i in range(te):
    elforce[i,0] = A * elstress[i,0]

print('\n\nMember Forces')
print(elforce)