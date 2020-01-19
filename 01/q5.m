%% 5) a)

communities = OpenDataCommunites('communities.data',-10000);
communities_novo = communities;


for i=1:1:size(communities,2)    
    [idl,~] = find(communities_novo(:,i) == -10000);
    linhas_desconsideradas(i) = length(idl);
end

idc = find(linhas_desconsideradas>10);
communities_novo(:,idc) = [];

%% 5) b)

tx_treino = round(0.7*length(communities_novo));
treino = communities_novo(1:tx_treino,:);
teste = communities_novo(tx_treino+1:end,:);

violencia = treino(:,end);
X = treino;
X(:,end)=1;
% X_novo = [X(:,end)'; X(:,1:end-1)']';
X_novo = X;

w = inv(X_novo'*X_novo)*X_novo'*violencia;

% teste_novo = [teste(:,end)'; teste(:,1:end-1)']';
teste_novo = teste;
teste_novo(:,end) = 1;

atributos_violencia = teste_novo;
atributos_violencia(:,end) = 1;

f_treino = X_novo*w;
f_teste =teste_novo(:,1:end)*w;

N_treino = size(treino,1);
N_teste = size(teste_novo,1);

denominador_0 = find(violencia==0);
violencia(denominador_0) = 0.01;

RMSE_treino = sqrt(sum((violencia-f_treino).^2)/N_treino)
RMSE_teste = sqrt(sum((teste(:,end)-f_teste).^2)/N_teste)

denominador_0 = find(teste(:,end)==0);
teste(denominador_0,:) = 0.01;

MAPE_treino = 100*sum(abs((violencia-f_treino)./violencia))/N_treino

N_teste = size(teste_novo,1);
f_teste =teste_novo*w;
MAPE_teste = 100*sum(abs((teste(:,end)-f_teste)./teste(:,end)))/N_teste



%% 5) c) 
treino_norm=[];
for j=1:size(treino,2)
    media = mean(treino(:,j));
    sd = std(treino(:,j));
    treino_norm(j,:) = (treino(:,j)' - media)/sd;
end
treino_norm = treino_norm';

N = size(treino_norm,1);
C = (treino_norm'*treino_norm)/(N-1);
L = (treino_norm*treino_norm')/(N-1);
[V,D] = eig(C);

lambda = diag(D);

format long
[lambda_decrease,I] = sort(lambda,'descend');
V_decrease = V(:,I);

% GRAFICO PARETO
pca = 5;
% figure
% pareto(lambda)
% title('Atributes')
yyaxis left
bar(lambda_decrease(1:pca)), hold on,
soma = [];
soma(1)=lambda_decrease(1);
for ii=2:pca
    soma(ii) = soma(ii-1)+lambda_decrease(ii);
end
yyaxis right
plot(100*soma/sum(lambda_decrease),'k.-')
scatter(1:pca,100*soma/sum(lambda_decrease),'ko','filled')

media = 0;
teste_norm=[];
for j=1:size(teste,2)
    media = mean(teste(:,j));
    sd = std(teste(:,j));
    teste_norm(j,:) = (teste(:,j)' - media)/sd;
end

teste_norm = teste_norm';

treino_pca = V_decrease(:,1:pca)'*treino_norm';
teste_pca = V_decrease(:,1:pca)'*teste_norm';

treino_pca = treino_pca';
teste_pca = teste_pca';

X = treino_pca;
X(:,end)=1;
X_pca = X;
w_pca = inv(X_pca'*X_pca)*X_pca'*violencia;

teste_novo = teste_pca;
teste_novo(:,end) = 1;

f_treino_pca = X_pca*w_pca;
f_teste_pca =teste_novo(:,1:end)*w_pca;

RMSE_treino_pca = sqrt(sum((violencia-f_treino_pca).^2)/N_treino)
RMSE_teste_pca = sqrt(sum((teste(:,end)-f_teste_pca).^2)/N_teste)

denominador_0 = find(teste(:,end)==0);
teste(denominador_0,:) = 0.01;

MAPE_treino_pca = 100*sum(abs((violencia-f_treino_pca)./violencia))/N_treino

N_teste = size(teste_novo,1);
f_teste_pca =teste_novo*w_pca;
MAPE_teste_pca = 100*sum(abs((teste(:,end)-f_teste_pca)./teste(:,end)))/N_teste

