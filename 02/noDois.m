function [index,i11,i12,i21,i22,i41,i42] = noDois(ctreino,atreino)
% SD CLASSE
sdClasse = sd(ctreino);
% Atributo 01: x <= 2; x > 2;
[i11,~] = find(atreino(:,1)<=2);
[i12,~] = find(atreino(:,1)>2);
a11 = atreino(i11,1);
a12 = atreino(i12,1);
SDR1 = sdClasse - (length(a11)/size(atreino,1))*sd(a11) - (length(a12)/size(atreino,1))*sd(a12);
% Atributo 02: x <= 3; x > 3;
[i21,~] = find(atreino(:,2)<=3);
[i22,~] = find(atreino(:,2)>3);
a21 = atreino(i21,2);
a22 = atreino(i22,2);
SDR2 = sdClasse - (length(a21)/size(atreino,1))*sd(a21) - (length(a22)/size(atreino,1))*sd(a22);
% Atributo 04: x <= 4; x > 4;
[i41,~] = find(atreino(:,4)<=4);
[i42,~] = find(atreino(:,4)>4);
a41 = atreino(i41,4);
a42 = atreino(i42,4);
SDR4 = sdClasse - (length(a41)/size(atreino,1))*sd(a41) - (length(a42)/size(atreino,1))*sd(a42);
% SDR TODOS
SDRF = [SDR1,SDR2,SDR4];
[SDRF,index] = max(SDRF);