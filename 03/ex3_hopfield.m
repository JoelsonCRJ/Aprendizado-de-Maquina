function [vFinal] = ex3_hopfield(w,y1)

v = [y1'];
k = 1;
flag = 0;
while flag == 0
    diferentes = 0;
    for i = 1:size(v,2)
        vetorI(:,i) = w(:,i).*v(k,i);
    end
    somaI = sum(vetorI,2);
    compara(somaI>=0) = 1;
    compara(somaI<0) = -1;
    v = [v;compara];
    diferentes = sum(v(k,:)~=v(k+1,:));
    if diferentes == 0
        flag = 1;
    end
    k = k + 1;
end
vFinal = v(end,:);