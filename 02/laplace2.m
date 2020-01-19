function [ACC] = laplace2(teste,treino)
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

% Probabilidade de cada classe
prob1 = size(classe1,1)/size(atribtreino,1);
prob0 = size(classe0,1)/size(atribtreino,1);

% Separação em 4 bins
for i = 1:size(classe0,2)
    bins0(i,:) = [sum(classe0(:,i)==1),sum(classe0(:,i)==2),sum(classe0(:,i)==3),...
        sum(classe0(:,i)==4)];
    bins1(i,:) = [sum(classe1(:,i)==1),sum(classe1(:,i)==2),sum(classe1(:,i)==3),...
        sum(classe1(:,i)==4)];
end

soma1 = sum(bins1(1,:));
soma0 = sum(bins0(1,:));

% TESTE
atributoteste = teste(:,2:end);
classeteste = teste(:,1);
for j = 1:size(atributoteste,2)
    for i = 1:size(atributoteste,1)
        v = atributoteste(i,j);
        p1(i,j)=(bins1(j,v)+1)/(soma1+4);
        p0(i,j)=(bins0(j,v)+1)/(soma0+4);
    end
end

% Probabilidade
pf1 = 1; pf0 = 1;
for k = 1:size(prob1,2)
    pf1 = pf1.*p1(:,k);
    pf0 = pf0.*p0(:,k);
end

pf1 = pf1*prob1;
pf0 = pf0*prob0;

% Rótulo
for m = 1:size(pf1,1)
    if pf1(m,1) > pf0(m,1)
        rotulo(m,1) = 1;
    else
        rotulo(m,1) = 0;
    end
end

% Acurácia
count = 0;
for n = 1:size(rotulo,1)
    if rotulo(n,1) == classeteste(n,1)
        count = count + 1;
    end
end
ACC = count/n*100;


