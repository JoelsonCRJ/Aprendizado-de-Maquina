% Programa de Pós-Graduação em Engenharia Elétrica
% Leticia Araújo Silva
% Lista 02
% Exercício 06

close all, clear all, clc

% 1. motor: A,B,C,D,E = 1,2,3,4,5
% 2. screw: A,B,C,D,E = 1,2,3,4,5
% 3. pgain: 3,4,5,6
% 4. vgain: 1,2,3,4,5
% 5. class: 0.13 to 7.10

data = importdata('servo.data');
texto = string(data.textdata);
dados = zeros(size(texto,1),size(texto,2));
valores = data.data;

% Mudança da Classe para Numérica
for j = 1:size(texto,2)
    for i = 1:size(texto,1)
        if texto(i,j) == 'A'
            dados(i,j) = 1;
        elseif texto(i,j) == 'B'
            dados(i,j) = 2;
        elseif texto(i,j) == 'C'
            dados(i,j) = 3;
        elseif texto(i,j) == 'D'
            dados(i,j) = 4;
        elseif texto(i,j) == 'E'
            dados(i,j) = 5;
        end
    end
end

atributos = [dados,valores(:,1:2)];
classes = valores(:,3);

atreino = atributos(1:ceil(0.75*size(atributos,1)),:);
ctreino = classes(1:ceil(0.75*size(classes,1)),:);

ateste = atributos(ceil(0.75*size(atributos,1))+1:end,:);
cteste = classes(ceil(0.75*size(classes,1))+1:end,:);

%% LETRA A
% PRIMEIRO NÓ
[index1,a31,a32] = noUm(ctreino,atreino);
% SEGUNDO NÓ:
% Novos conjuntos de Treino
natreinoMenor = atreino(a31,:);
nctreinoMenor = ctreino(a31,:);
natreinoMaior = atreino(a32,:);
nctreinoMaior = ctreino(a32,:);
% Para Atributo 3 <= 4
[index2Menor,~,~,~,~,i41,i42]  = noDois(nctreinoMenor,natreinoMenor);
% Para Atributo 3 > 4
[index2Maior,~,~,i21,i22,~,~]  = noDois(nctreinoMaior,natreinoMaior);
% ÁRVORE REGRESSÃO
[l1,~] = find(atreino(:,3)<=5 & atreino(:,4)<=4);
media1 = mean(ctreino(l1,1));
[l2,~] = find(atreino(:,3)<=5 & atreino(:,4)>4);
media2 = mean(ctreino(l2,1));
[l3,~] = find(atreino(:,3)>5 & atreino(:,2)<=3);
media3 = mean(ctreino(l3,1));
[l4,~] = find(atreino(:,3)>5 & atreino(:,2)>3);
media4 = mean(ctreino(l4,1));

%% LETRA B
for i = 1:size(ateste,1)
    if ateste(i,3) <= 4
        if ateste(i,4) <= 4
            rotulo(i,1) = media1;
        elseif ateste(i,4) > 4
            rotulo(i,1) = media2;
        end
    elseif ateste(i,3) > 4
        if ateste(i,2) <= 3
            rotulo(i,1) = media3;
        elseif ateste(i,2) > 3
            rotulo(i,1) = media4;
        end
    end
end

% MAPE
MAPE = sum(abs(cteste-rotulo)./abs(cteste))/length(cteste)*100;
fprintf('MAPE = %0.2f%%\n',MAPE)
RMSE = sqrt(sum((cteste-rotulo).^2)/length(cteste));
fprintf('RMSE = %0.2f\n',RMSE)