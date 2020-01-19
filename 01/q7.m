arquivo = 'magic04.data';

magic = importdata(arquivo,'%s');
length_magic = length(magic);

formatSpec = '%f %f %f %f %f %f %f %f %f %f %s';

fileID = fopen(arquivo);
cell_magic = textscan(fileID,formatSpec,length_magic,'Delimiter',',','CollectOutput',0);

data_magic = [];
for i = 1:(size(cell_magic,2))
    data_magic(i,:) = (cell_magic{1,i})';
end

data_magic = data_magic';

% DIVIDIR EM TREINO, VALIDACAO E TESTE
id_rand = randperm(19020);
id_treino = id_rand(1:length_magic/3);
id_validacao = id_rand((length_magic/3)+1:2*length_magic/3);
id_teste = id_rand((2*length_magic/3)+1:end);

treino_magic = data_magic(id_treino,:);
validacao_magic = data_magic(id_validacao,:);
teste_magic = data_magic(id_teste,:);

formatSpec = '%*f %*f %*f %*f %*f %*f %*f %*f %*f %*f %s';

fileID = fopen(arquivo);
cell_classe_magic = textscan(fileID,formatSpec,length_magic,'Delimiter',',','CollectOutput',0);

% DEFINIR AS CLASSES (0-signal 1-background)
data_classe_magic = string(cell_classe_magic{1,1});
[id0,~] = find(data_classe_magic=='g');
[id1,~] = find(data_classe_magic=='h');

classe_magic(id0) = 0;
classe_magic(id1) = 1;

classe_magic_treino = classe_magic(id_treino);
classe_magic_validacao = classe_magic(id_validacao);
classe_magic_teste = classe_magic(id_teste);

%% a) SFS

U=[];
arg = [1:size(data_magic,2)]
aux2 = 1;
diff_sig = 10000;    
anterior(1) = 0;

% while diff_sig > 0
for aux2=1:6
    accuracyNN=[];
    d_euclidiana=[];
    for k=arg
    % NN
    aux = [];
    classe_nn = [];
    conf_mat=[];
    for i=1:size(validacao_magic,1)
        for j = 1:size(treino_magic,1)
            d_euclidiana(j) = sqrt(sum((validacao_magic(i,[U,k])-treino_magic(j,[U,k])).^2));
        end
    [~,id_min] = min(d_euclidiana);   
    classe_nn(i) = classe_magic_treino(id_min);
    end

    [~,idx_0] = find(classe_nn==0);
    idx_0_correct = find((classe_nn(idx_0)-classe_magic_validacao(idx_0))==0);
    VN = length(idx_0_correct);
    FN = length(idx_0)-VN;

    [~,idx_1] = find(classe_nn==1);
    idx_1_correct = find((classe_nn(idx_1)-classe_magic_validacao(idx_1))==0);
    VP = length(idx_1_correct);
    FP = length(idx_1)-VP;

    conf_mat = [VP FP; FN VN];
    TP = sum(diag(conf_mat));
    accuracyNN(k) = 100*(VP+VN)/(VP+VN+FN+FP)
    end
[max_acc,id_max_arg] = max(accuracyNN);
U(aux2) = id_max_arg;
arg(find(arg==id_max_arg))=[];
% anterior(aux2+1) = max_acc;
% diff_sig = max_acc - anterior(aux2);
% aux2  = aux2+1;
end

%% NN SOBRE O TESTE

novo_treino_magic = [treino_magic(:,sort(U));validacao_magic(:,sort(U))];
nova_classe_magic_treino = [classe_magic_treino';classe_magic_validacao']';

% NN
aux = [];
classe_nn = [];
d_euclidiana=[];
for i=1:size(teste_magic,1)
    for j = 1:size(novo_treino_magic,1)
        d_euclidiana(j) = sqrt(sum((teste_magic(i,sort(U))-novo_treino_magic(j,:)).^2));
    end
[~,id_min] = min(d_euclidiana);   
classe_nn(i) = nova_classe_magic_treino(id_min);
end

[~,idx_0] = find(classe_nn==0);
idx_0_correct = find((classe_nn(idx_0)-classe_magic_teste(idx_0))==0);
VN = length(idx_0_correct);
FN = length(idx_0)-VN;

[~,idx_1] = find(classe_nn==1);
idx_1_correct = find((classe_nn(idx_1)-classe_magic_teste(idx_1))==0);
VP = length(idx_1_correct);
FP = length(idx_1)-VP;

conf_mat = [VP FP; FN VN];
TP = sum(diag(conf_mat));
accuracyNN = 100*(VP+VN)/(VP+VN+FN+FP)

%% a) SBS

U=[];
arg = [1:size(data_magic,2)]
aux2 = 1;
diff_sig = 10000;    
anterior(1) = 0;

% while diff_sig > 0
for aux2=1:(size(data_magic,2)-6)
    accuracyNN=[];
    d_euclidiana=[];
    aux3=1;
    arg_aux=arg;
    for k=arg_aux
    % NN
    aux = [];
    classe_nn = [];
    conf_mat=[];
    for i=1:size(validacao_magic,1)
        for j = 1:size(treino_magic,1)
            d_euclidiana(j) = sqrt(sum((validacao_magic(i,arg_aux)-treino_magic(j,arg_aux)).^2));
        end
    [~,id_min] = min(d_euclidiana);   
    classe_nn(i) = classe_magic_treino(id_min);
    end

    [~,idx_0] = find(classe_nn==0);
    idx_0_correct = find((classe_nn(idx_0)-classe_magic_validacao(idx_0))==0);
    VN = length(idx_0_correct);
    FN = length(idx_0)-VN;

    [~,idx_1] = find(classe_nn==1);
    idx_1_correct = find((classe_nn(idx_1)-classe_magic_validacao(idx_1))==0);
    VP = length(idx_1_correct);
    FP = length(idx_1)-VP;

    conf_mat = [VP FP; FN VN];
    TP = sum(diag(conf_mat));
    accuracyNN(k) = 100*(VP+VN)/(VP+VN+FN+FP)
    arg_aux(aux3)=[];
    end
[min_acc,id_min_arg] = min(accuracyNN);
U(aux2) = id_min_arg;
arg(find(arg==id_min_arg))=[];
% anterior(aux2+1) = max_acc;
% diff_sig = max_acc - anterior(aux2);
% aux2  = aux2+1;
end

%% NN SOBRE O TESTE

novo_treino_magic = [treino_magic(:,arg);validacao_magic(:,arg)];
nova_classe_magic_treino = [classe_magic_treino';classe_magic_validacao']';

% NN
aux = [];
classe_nn = [];
d_euclidiana=[];
for i=1:size(teste_magic,1)
    for j = 1:size(novo_treino_magic,1)
        d_euclidiana(j) = sqrt(sum((teste_magic(i,arg)-novo_treino_magic(j,:)).^2));
    end
[~,id_min] = min(d_euclidiana);   
classe_nn(i) = nova_classe_magic_treino(id_min);
end

[~,idx_0] = find(classe_nn==0);
idx_0_correct = find((classe_nn(idx_0)-classe_magic_teste(idx_0))==0);
VN = length(idx_0_correct);
FN = length(idx_0)-VN;

[~,idx_1] = find(classe_nn==1);
idx_1_correct = find((classe_nn(idx_1)-classe_magic_teste(idx_1))==0);
VP = length(idx_1_correct);
FP = length(idx_1)-VP;

conf_mat = [VP FP; FN VN];
TP = sum(diag(conf_mat));
accuracyNN = 100*(VP+VN)/(VP+VN+FN+FP)
