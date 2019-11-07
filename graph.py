from pylab import *

# Shaft extension
xmax = 10.0
xmin = -xmax
ymax = 10.0
ymin = -ymax

# Point for shaft
NX = 10
NY = 10

# Define shaft
x = linspace(xmin, xmax, NX)
y = linspace(ymin, ymax, NY)

# Define coordinates
X, Y = meshgrid(x, y)

# Define function
Bx = Y**2
By = X**2

# Draw
figure()
QP = quiver(X, Y, Bx, By)
quiverkey(QP, 0.85, 1.05, 1.0, '1m', labelpos='N')
# dx = (xmax-xmin)/(NX-1)
# dy = (ymax-ymin)/(NY-1)
# axis([xmin-dx, xmax+dx, ymin-dy, ymax+dy])
title('Campo vectorial')
xlabel('X')
ylabel('Y')
show()