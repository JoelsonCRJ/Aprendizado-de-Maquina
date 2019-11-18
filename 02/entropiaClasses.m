function [EC] = entropiaClasses(ctreino,classes)

% Probabilidade de cada classe (cada coluna é uma classe)

for i = 1:length(classes)
    pC(1,i) = sum(ctreino==classes(i))/length(ctreino);
end
% Entropia de cada classe (cada coluna é a entropia de uma classe)
for k = 1:length(pC)
    EC(k) = -pC(k)*log2(pC(k));
end
% Substituindo valores NaN por Zero
for m = 1:length(EC)
    if any(isnan(EC(m)))
        EC(m)=0;
    end
end
% Entropia das Classes
EC = sum(EC);