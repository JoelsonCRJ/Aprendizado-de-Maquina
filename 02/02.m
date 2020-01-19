close all, clear all, clc

% TREINO
data1 = importdata('monks-2.train');
splitcells1 = regexp(data1, '\t', 'split');
splitcells1 = string(vertcat(splitcells1{:}));
treino = split(splitcells1);
treino = double(treino(:,2:8));

% TESTE
data2 = importdata('monks-2.test');
splitcells2 = regexp(data2, '\t', 'split');
splitcells2 = string(vertcat(splitcells2{:}));
teste = split(splitcells2);
teste = double(teste(:,2:8));

% LETRA A
ACCa = gaussiana2(teste,treino);
fprintf('Acurácia letra a = %0.2f%%\n',ACCa)

% LETRA B
ACCb = discretizar2(teste,treino);
fprintf('Acurácia letra b = %0.2f%%\n',ACCb)

% LETRA C
ACCc = laplace2(teste,treino);
fprintf('Acurácia letra c = %0.2f%%\n',ACCc)


