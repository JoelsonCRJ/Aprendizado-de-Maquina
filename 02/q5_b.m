close all
clear all
clc

data = importdata('nursery.data');
splitcells1 = regexp(data, ',', 'split');
splitcells1 = string(vertcat(splitcells1{:}));
dados = string(split(splitcells1));

ateste = dados(1001:end,1:8);       % Atributos Teste
cteste = dados(1001:end,9);         % Classes Teste

for i = 1:size(ateste,1)
    %     Nó 01
    if ateste(i,8) == "priority"
        rotulo(i,1) = "priority";
    elseif ateste(i,8) == "not_recom"
        rotulo(i,1) = "not_recom";
    elseif ateste(i,8) == "recommended"
        if ateste(i,7) == "slightly_prob"
            rotulo(i,1) = "priority";
        elseif ateste(i,7) == "problematic"
            rotulo(i,1) = "priority";
        end
    else
        rotulo(i,1) = "vazio"
    end
end

ACC = sum(rotulo==cteste)/size(rotulo,1)*100;
