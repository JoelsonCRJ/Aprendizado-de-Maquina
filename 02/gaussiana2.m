function [ACC] = gaussiana2(teste,treino)
% TREINO
classetreino = treino(:,1);
atribtreino = treino(:,2:end);
% Separar em Classes
c0 = 1; c1 = 1;
for i = 1:size(classetreino,1)
    if classetreino(i,1) == 1
        classe1(c1,:) = atribtreino(i,:);
        c1 = c1 + 1;
    elseif classetreino(i,1) == 0
        classe0(c0,:) = atribtreino(i,:);
        c0 = c0 + 1;
    end
end

% Média, Desvio Padrão e Probabilidade de cada classe
media1 = mean(classe1);
desvio1 = std(classe1);
prob1 = size(classe1,1)/size(atribtreino,1);
media0 = mean(classe0);
desvio0 = std(classe0);
prob0 = size(classe0,1)/size(atribtreino,1);

atributoteste = teste(:,2:end);
classeteste = teste(:,1);

% Gaussiana
for j = 1:size(atributoteste,2)
    for i = 1:size(atributoteste,1)
        x = atributoteste(i,j);
        pGaus1(i,j) = pGaussiana(x,media1(1,j),desvio1(1,j));
        pGaus0(i,j) = pGaussiana(x,media0(1,j),desvio0(1,j));
    end
end

% Probabilidade
pf1 = 1; pf0 = 1;
for k = 1:size(pGaus1,2)
    pf1 = pf1.*pGaus1(:,k);
    pf0 = pf0.*pGaus0(:,k);
end

pf = [pf0*prob0,pf1*prob1];

% Rótulo
for m = 1:size(pf,1)
    if pf(m,1) > pf(m,2)
        rotulo(m,1) = 0;
    else
        rotulo(m,1) = 1;
    end
end

% Acurácia
ACC = sum(rotulo==classeteste)/size(rotulo,1)*100;

