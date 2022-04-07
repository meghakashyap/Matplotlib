import matplotlib.pyplot as plt 
import numpy as np 
xcoordinates=np.array([18,11,0,2,1,0]) 
plt.plot(xcoordinates,linestyle='dotted') 
plt.show() 

xcoordinates=np.array([18,11,0,2,1,0]) 
plt.plot(xcoordinates,ls='dashdot',c='r',linewidth=20.5) 
plt.show() 

xcoordinates=np.array([18,11,0,2,1,0]) 
xcoordinates1=np.array([98,67,41,23,41,67]) 
plt.plot(xcoordinates,ls='dashdot',c='r',linewidth=20.5) 
plt.plot(xcoordinates1,ls='dashdot',c='hotpink',linewidth=20.5) 
plt.show() 

xcoordinates1=np.array([18,11,0,2,1,0])
ycoordinates1=np.array([98,67,41,23,41,67]) 
xcoordinates2=np.array([8,1,0,1,9,1]) 
ycoordinates2=np.array([8,7,1,2,4,6]) 
plt.plot(xcoordinates,ycoordinates1,xcoordinates2,ycoordinates2)
plt.show() 

xcoordinates1=np.array([18,11,0,2,1,0]) 
ycoordinates1=np.array([98,67,41,23,41,67]) 
xcoordinates2=np.array([8,1,0,1,9,1])
ycoordinates2=np.array([8,7,1,2,4,6]) 

plt.plot(xcoordinates,ycoordinates1,xcoordinates2,ycoordinates2)

font1 = {'family':'serif','color':'blue','size':20} 
font2 = {'family':'serif','color':'darkred','size':15} 

plt.title("this is my chart",fontdict=font1,loc='right')
plt.xlabel("this is x axis",fontdict=font2) 
plt.ylabel("this is y axis",fontdict=font2) 
plt.grid(axis='y',color='red',ls='dashdot',linewidth=10)

plt.show() 