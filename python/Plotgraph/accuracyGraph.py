import matplotlib.pyplot as pp

xCor = [10,50,200,400,600]
yCor = [0.919,0.927,0.9396499418892215,0.945668734828615,0.9564178525312873]

pp.ylim(0.9,1)
pp.xlim(10,600)

pp.plot(xCor,yCor);

pp.ylabel('Number of documents in model')
pp.xlabel('Accuracy in percentage')
     
pp.show()
