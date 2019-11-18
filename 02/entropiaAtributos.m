function [Eatrib] = entropiaAtributos(a1,atreino,ctreino,coluna)
% Atributo 01
% a1 = ["usual","pretentious", "great_pret"];
classes =  ["not_recom","recommend","very_recom","priority","spec_prior"];
% Probabilidade de cada atribuição possível do atributo (cada coluna é
% uma classe)
for j = 1:length(classes)
    for i = 1:length(a1)
        prob1(i,j) = sum(atreino(:,coluna)==a1(i) & ctreino==classes(j))/sum(atreino(:,coluna)==a1(i));
    end
end
% Entropia de cada atribuição possível do atributo(cada coluna é uma
% classe)
for k = 1:size(prob1,1)
    for m = 1:size(prob1,2)
        h1(k,m) = -prob1(k,m)*log2(prob1(k,m));
    end
end
% Retirando valores NaN de cada atribuição possível do atributo(cada
% linha é de uma possível atribuição)
for x = 1:size(h1,1)
    for y = 1:size(h1,2)
        if any(isnan(h1(x,y)))
            h1(x,y)=0;
        end
    end
end
% Entropia final de cada atribuição possível do atributo (cada linha é
% de uma possível atribuição)
nh1 = sum(h1,2);
% Probabilidade de cada possível atribuição
for i = 1:length(a1)
    p1(i,1) = sum(atreino(:,coluna)==a1(i))/size(atreino,1);
end
e = p1.*nh1;
% Entropia do Atributo
Eatrib = sum(e);