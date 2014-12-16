import matplotlib.pyplot as pp

xCor = [1,5,10,15,20,25,30,50,100,200,400,600]
yCor = [0.0136,0.480,2.4758,4.623,9.952,17.572,27.081,79.78,330.98,1556,5843,10331.5914]

pp.ylim(min(yCor)-1,max(yCor)+1)
pp.xlim(min(xCor)-1,max(xCor)+1)

pp.plot(xCor,yCor);

pp.ylabel('Time in seconds')
pp.xlabel('Number of documents')
     
pp.title('Time/document graph')
pp.show()
