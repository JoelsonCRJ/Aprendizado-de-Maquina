htru2 = importdata('HTRU_2.txt','%s');

length_htru2 = length(htru2);

formatSpec = '%f %f %f %f %f %f %f %f %d';

fileID = fopen('HTRU_2.txt');
cell_htru2 = textscan(fileID,formatSpec,length_htru2,'Delimiter',',','HeaderLines',11,'CollectOutput',0);
data_htru2 = double([cell_htru2{1,1}';cell_htru2{1,2}';cell_htru2{1,3}';cell_htru2{1,4}';cell_htru2{1,5}';cell_htru2{1,6}';cell_htru2{1,7}';cell_htru2{1,8}';cell_htru2{1,9}']');
 
id = randperm(length(data_htru2));

id_treino = id(1:6000);
id_teste = id(6001:end);

treino_htru2 = data_htru2(id_treino,:);
teste_htru2 = data_htru2(id_teste,:);

classe_treino = treino_htru2(:,end);
classe_teste = teste_htru2(:,end);

data_treino_htru2 = treino_htru2(:,1:end-1);
data_teste_htru2 = teste_htru2(:,1:end-1);

%% 6) a)

% ROCCHIO
tic
numclass = 2;
mi_i = [];
for i = 1:numclass
    mi_i(i,:) = mean(data_treino_htru2(find(classe_treino==(i-1)),:));
end

d_mahala = [];
M_eps = cov(data_teste_htru2);
for i=1:size(data_teste_htru2,1)
    for j = 1:size(mi_i,1)   
        d_mahala(j) = sqrt((data_teste_htru2(i,:)-mi_i(j,:))*inv(M_eps)*(data_teste_htru2(i,:)-mi_i(j,:))');
    end
[~,b] = min(d_mahala);
classe_rocchio(i) = b-1;    
end


[~,idx_0] = find(classe_rocchio==0);
idx_0_correct = find((classe_rocchio(idx_0)'-classe_teste(idx_0))==0);
VN = length(idx_0_correct);
FN = length(idx_0)-VN;

[~,idx_1] = find(classe_rocchio==1);
idx_1_correct = find((classe_rocchio(idx_1)'-classe_teste(idx_1))==0);
VP = length(idx_1_correct);
FP = length(idx_1)-VP;

conf_mat = [VP FP; FN VN];
TP = sum(diag(conf_mat));
accuracyR = 100*(VP+VN)/(VP+VN+FN+FP)
recallR=100*TP/(TP+FN)
precisionR=100*TP/(TP+FP)

%%  6) b)

N_treino = size(data_treino_htru2,1);
treino = data_treino_htru2(1:N_treino/2,:);
validacao = data_treino_htru2(N_treino/2+1:end,:);

classe_treino = treino_htru2(1:N_treino/2,end);
classe_validacao = treino_htru2(N_treino/2+1:N_treino,end);

% kNN
kmax=100;
accuracyNN = [];
precisionNN = [];
recallNN = [];
for k=2:kmax
aux = [];
classe_nn = [];
for i=1:size(validacao,1)
    for j = 1:size(treino,1)   
        d_euclidiana(j) = sqrt(sum((validacao(i,:)-treino(j,:)).^2));
    end
[~,id_desc] = sort(d_euclidiana);   
    for kk=1:k
        aux(kk,i) = classe_treino(id_desc(kk));   
    end
[~,z] = find(aux(:,i)==0);
    if length(z)>=kmax/2
        classe_nn(i) = 0;
    else
        classe_nn(i) = 1;
    end
end

[~,idx_0] = find(classe_nn==0);
idx_0_correct = find((classe_nn(idx_0)'-classe_validacao(idx_0))==0);
VN = length(idx_0_correct);
FN = length(idx_0)-VN;

[~,idx_1] = find(classe_nn==1);
idx_1_correct = find((classe_nn(idx_1)'-classe_validacao(idx_1))==0);
VP = length(idx_1_correct);
FP = length(idx_1)-VP;

conf_mat = [VP FP; FN VN];
TP = sum(diag(conf_mat));
accuracyNN(k) = 100*(VP+VN)/(VP+VN+FN+FP);
precisionNN(k)=100*TP/(TP+FP);
recallNN(k)=100*TP/(TP+FN);

end


%%

[maior_acc,id_acc] = max(accuracyNN);
[maior_pre,id_pre] = max(precisionNN);
[maior_rec,id_rec] = max(recallNN);

matriz_avaliacao = [accuracyNN;precisionNN;recallNN];
% fprintf('Melhor k: %d\n', best_k)
media_avaliacao = mean(matriz_avaliacao,1);
[melhor_media,id_mm] = max(media_avaliacao)

%%
k = id_mm;
aux = [];
classe_nn = [];
for i=1:size(validacao,1)
    for j = 1:size(treino,1)   
        d_euclidiana(j) = sqrt(sum((validacao(i,:)-treino(j,:)).^2));
    end
[~,id_desc] = sort(d_euclidiana);   
    for kk=1:k
        aux(kk,i) = classe_treino(id_desc(kk));   
    end
[~,z] = find(aux(:,i)==0);
    if length(z)>=kmax/2
        classe_nn(i) = 0;
    else
        classe_nn(i) = 1;
    end
end

[~,idx_0] = find(classe_nn==0);
idx_0_correct = find((classe_nn(idx_0)'-classe_validacao(idx_0))==0);
VN = length(idx_0_correct);
FN = length(idx_0)-VN;

[~,idx_1] = find(classe_nn==1);
idx_1_correct = find((classe_nn(idx_1)'-classe_validacao(idx_1))==0);
VP = length(idx_1_correct);
FP = length(idx_1)-VP;

conf_mat = [VP FP; FN VN];
TP = sum(diag(conf_mat));
accuracyNN = 100*(VP+VN)/(VP+VN+FN+FP);
precisionNN=100*TP/(TP+FP);
recallNN=100*TP/(TP+FN);

