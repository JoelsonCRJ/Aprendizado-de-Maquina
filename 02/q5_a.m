close all
clear all
clc

data = importdata('nursery.data');
splitcells1 = regexp(data, ',', 'split');
splitcells1 = string(vertcat(splitcells1{:}));
dados = string(split(splitcells1));

atreino = dados(1:1000,1:8);        % Atributos Treino
ctreino = dados(1:1000,9);          % Classes Treino
% ateste = dados(1001:end,1:8);       % Atributos Teste
% cteste = dados(1001:end,9);         % Classes Teste

a1 = ["usual","pretentious", "great_pret"];
a2 = ["proper", "less_proper", "improper", "critical", "very_crit"];
a3 = ["complete", "completed", "incomplete", "foster"];
a4 = ["1", "2", "3", "more"];
a5 = ["convenient", "less_conv", "critical"];
a6 = ["convenient", "inconv"];
a7 = ["non-prob", "slightly_prob", "problematic"];
a8 = ["recommended", "priority", "not_recom"];
classes =  ["not_recom","recommend","very_recom","priority","spec_prior"];

%% NÓ 01
EC = entropiaClasses(ctreino,classes);
Eatrib1 = entropiaAtributos(a1,atreino,ctreino,1);
Eatrib2 = entropiaAtributos(a2,atreino,ctreino,2);
Eatrib3 = entropiaAtributos(a3,atreino,ctreino,3);
Eatrib4 = entropiaAtributos(a4,atreino,ctreino,4);
Eatrib5 = entropiaAtributos(a5,atreino,ctreino,5);
Eatrib6 = entropiaAtributos(a6,atreino,ctreino,6);
Eatrib7 = entropiaAtributos(a7,atreino,ctreino,7);
Eatrib8 = entropiaAtributos(a8,atreino,ctreino,8);
IG = [EC - Eatrib1,EC - Eatrib2,EC - Eatrib3,EC - Eatrib4,EC - Eatrib5,...
    EC - Eatrib6,EC - Eatrib7,EC - Eatrib8];
% Primeiro nó
[ganho,atributo] = max(IG);
a0 = zeros(length(a8),5);

% Classificação utilizando o atributo 08: cada coluna é uma classe e cada
% linha é um subconjunto do atributo 08
for k = 1:length(classes)    
    for i = 1:length(ctreino)
        if (ctreino(i) == classes(k))
            for n = 1:length(a8)
                if (atreino(i,8) == a8(n))
                    a0(n,k) = a0(n,k)+1;
                end
            end
        end
    end
end

% Verificar se há classes já separadas
count = zeros(size(a0,1),1);
for i = 1:size(a0,1)
    for j = 1:size(a0,2)
        if a0(i,j) == 0
            count(i,1) = count(i,1) + 1;
        end
    end
end
cSeparar = [];
lSeparar = [];
for k = 1:length(count)
    if count(k) == 4                % Maximo de classes - 1
        [~,c] = find(a0(k,:)~=0);
        cSeparar = [cSeparar,c];
        lSeparar = [lSeparar,k];
    end
end

%% NÓ 2
a1 = ["usual","pretentious", "great_pret"];
a2 = ["proper", "less_proper", "improper", "critical", "very_crit"];
a3 = ["complete", "completed", "incomplete", "foster"];
a4 = ["1", "2", "3", "more"];
a5 = ["convenient", "less_conv", "critical"];
a6 = ["convenient", "inconv"];
a7 = ["non-prob", "slightly_prob", "problematic"];
classes =  ["not_recom","recommend","very_recom","priority","spec_prior"];

% Novo Conjunto de Treino
nTreino = [];
nClasses = [];
for i = 1:size(atreino,1)
    if atreino(i,8) == "recommended"
        an = atreino(i,1:7);
        nTreino = [nTreino;an];
        cn = ctreino(i,1);
        nClasses = [nClasses;cn];
    end
end

% Novos Cálculos de Entropia
EC_2 = entropiaClasses(classes,classes);
Eatrib1_2 = entropiaAtributos(a1,nTreino,nClasses,1);
Eatrib2_2 = entropiaAtributos(a2,nTreino,nClasses,2);
Eatrib3_2 = entropiaAtributos(a3,nTreino,nClasses,3);
Eatrib4_2 = entropiaAtributos(a4,nTreino,nClasses,4);
Eatrib5_2 = entropiaAtributos(a5,nTreino,nClasses,5);
Eatrib6_2 = entropiaAtributos(a6,nTreino,nClasses,6);
Eatrib7_2 = entropiaAtributos(a7,nTreino,nClasses,7);
IG_2 = [EC_2 - Eatrib1_2,EC_2 - Eatrib2_2,EC_2 - Eatrib3_2,EC_2 - Eatrib4_2...
    ,EC_2 - Eatrib5_2,EC_2 - Eatrib6_2,EC_2 - Eatrib7_2];
[ganho_2,atributo_2] = max(IG_2);

% Classificação utilizando o atributo 07: cada coluna é uma classe e cada
% linha é um subconjunto do atributo 07
a0_2 = zeros(length(a7),5);

for k = 1:length(classes)    
    for i = 1:length(ctreino)
        if (ctreino(i) == classes(k))
            for n = 1:length(a7)
                if (atreino(i,7) == a7(n))
                    a0_2(n,k) = a0_2(n,k)+1;
                end
            end
        end
    end
end
