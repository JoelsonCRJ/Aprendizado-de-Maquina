function [pGaus] = pGaussiana(x,media,desvio)

d1 = (-1/2)*(((x-media)/(desvio))^2);
e1 = 1/(desvio*sqrt(2*pi));
pGaus = e1*exp(d1);


