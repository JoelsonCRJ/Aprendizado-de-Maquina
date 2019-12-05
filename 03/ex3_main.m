close all, clear all, clc

% TREINAMENTO
B = double(imread('B.bmp'));
B = B(:);
U = double(imread('U.bmp'));
U = U(:);

% Mudança de 0 para -1
B(B==0) = -1;
U(U==0) = -1;

data = [B,U];
data = data';
w = zeros(size(data,2),size(data,2));
% Treinar rede
for i = 1:size(data,2)
    for j = 1:size(data,2)
        if i == j
            w(i,j) = 0;
        else
            w(i,j) = sum(data(:,i).*data(:,j));
        end
    end
end

% TESTE DA REDE
P = double(imread('P.bmp'));
P = P(:);
L = double(imread('L.bmp'));
L = L(:);
% Mudança de 0 para -1
P(P==0) = -1;
U(U==0) = -1;

% *********************** PARA LETRA: P *********************
[vP] = ex3_hopfield(w,P);
imshow(reshape(vP,9,7))
% *********************** PARA LETRA: L *********************
[vL] = ex3_hopfield(w,L);
figure,
imshow(reshape(vL,9,7))