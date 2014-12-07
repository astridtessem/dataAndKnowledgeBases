import matplotlib.pyplot as pp

xCor = [10,50,200,400]
yCor = [0.919,0.927,0.93,0.94]

pp.ylim(0.9,1)
pp.xlim(10,400)

pp.plot(xCor,yCor);

pp.ylabel('Number of documents in model')
pp.xlabel('Accuracy in percentage')
     
pp.show()
