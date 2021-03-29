clear
clc

dane = importdata('wifi_localization.txt');
N = length(dane);
N_tr = 1600;
N_te = N - N_tr;
res = ones(N_te,1);

%-----------------------------------------------------------------

%ZADANIE 1

% X_tr = dane(1:N_tr, 1:7);
% Y_tr = dane(1:N_tr, 8);
% X_te = dane(N_tr+1:end, 1:7);
% Y_te = dane(N_tr+1:end, 8);
% clknn = fitcknn(X_tr, Y_tr, 'NumNeighbors',5);
% y_validated = predict(clknn, X_te);
% 
% %subplot(2,2,1)
% figure
% k1=1;
% k2=2;
% hold on
% scatter(dane(dane(:,8)==1,k1), dane(dane(:,8)==1,k2), 'o','o')
% scatter(dane(dane(:,8)==2,k1), dane(dane(:,8)==2,k2), 'x','b')
% scatter(dane(dane(:,8)==3,k1), dane(dane(:,8)==3,k2), '+','g')
% scatter(dane(dane(:,8)==4,k1), dane(dane(:,8)==4,k2), '*','y')
% scatter(X_te(Y_te~=y_validated,k1),X_te(Y_te~=y_validated,k1), 300, 'X', 'r', 'LineWidth', 1)
% saveas(gcf, 'lipior_5_11.png')
% %subplot(2,2,2)
% figure
% k1=2;
% k2=3;
% hold on
% scatter(dane(dane(:,8)==1,k1), dane(dane(:,8)==1,k2), 'o','o')
% scatter(dane(dane(:,8)==2,k1), dane(dane(:,8)==2,k2), 'x','b')
% scatter(dane(dane(:,8)==3,k1), dane(dane(:,8)==3,k2), '+','g')
% scatter(dane(dane(:,8)==4,k1), dane(dane(:,8)==4,k2), '*','y')
% scatter(X_te(Y_te~=y_validated,k1),X_te(Y_te~=y_validated,k1), 300, 'X', 'r', 'LineWidth', 1)
% saveas(gcf, 'lipior_5_12.png')
% %subplot(2,2,1)
% figure
% k1=4;
% k2=5;
% hold on
% scatter(dane(dane(:,8)==1,k1), dane(dane(:,8)==1,k2), 'o','o')
% scatter(dane(dane(:,8)==2,k1), dane(dane(:,8)==2,k2), 'x','b')
% scatter(dane(dane(:,8)==3,k1), dane(dane(:,8)==3,k2), '+','g')
% scatter(dane(dane(:,8)==4,k1), dane(dane(:,8)==4,k2), '*','y')
% scatter(X_te(Y_te~=y_validated,k1),X_te(Y_te~=y_validated,k1), 300, 'X', 'r', 'LineWidth', 1)
% saveas(gcf, 'lipior_5_13.png')

%----------------------------------------------------------------

% ZADANIE 2

% NN = 100;
% 
% %Liczba sasiadow: k=1
% 
% suma_bledow = 0;
% 
% for i = 1:NN
%     data = dane;
%     data = data(randperm(N),:);
%     X_tr = data(1:N_tr, 1:7);
%     Y_tr = data(1:N_tr, 8);
%     X_te = data(N_tr+1:end, 1:7);
%     Y_te = data(N_tr+1:end, 8);
%     clknn = fitcknn(X_tr, Y_tr, 'NumNeighbors',1);
%     y_validated = predict(clknn, X_te);
%     blad = res(Y_te~=y_validated);
%     blad = length(blad);
%     suma_bledow = suma_bledow + blad;
% end
% blad_sredni_1_sasiad = suma_bledow/NN/N_te
% 
% %Liczba sasiadow: k=3
% 
% suma_bledow = 0;
% for i = 1:NN
%     data = dane;
%     data = data(randperm(N),:);
%     X_tr = data(1:N_tr, 1:7);
%     Y_tr = data(1:N_tr, 8);
%     X_te = data(N_tr+1:end, 1:7);
%     Y_te = data(N_tr+1:end, 8);
%     clknn = fitcknn(X_tr, Y_tr, 'NumNeighbors',3);
%     y_validated = predict(clknn, X_te);
%     blad = res(Y_te~=y_validated);
%     blad = length(blad);
%     suma_bledow = suma_bledow + blad;
% end
% blad_sredni_3_sasiadow = suma_bledow/NN/N_te
% 
% %Liczba sasiadow: k=4
% 
% suma_bledow = 0;
% for i = 1:NN
%     data = dane;
%     data = data(randperm(N),:);
%     X_tr = data(1:N_tr, 1:7);
%     Y_tr = data(1:N_tr, 8);
%     X_te = data(N_tr+1:end, 1:7);
%     Y_te = data(N_tr+1:end, 8);
%     clknn = fitcknn(X_tr, Y_tr, 'NumNeighbors',4);
%     y_validated = predict(clknn, X_te);
%     blad = res(Y_te~=y_validated);
%     blad = length(blad);
%     suma_bledow = suma_bledow + blad;
% end
% blad_sredni_4_sasiadow = suma_bledow/NN/N_te

%----------------------------------------------------------------

% ZADANIE 3
NN = 100;

% %Euclidesowa
% 
% %Liczba sasiadow: k=1
% suma_bledow_resubLoss = 0;
% suma_bledow_crossval = 0;
% suma_bledow_kfoldLoss = 0;
% for i = 1:NN
%     data = dane;
%     data = data(randperm(N),:);
%     X = data(:, 1:7);
%     Y = data(:, 8);
%     clknn = fitcknn(X, Y, 'NumNeighbors',1);
%     %clknn = fitcknn(X, Y, 'NumNeighbors',1, 'Distance', 'mahalanobis');
%     blad = resubLoss(clknn);
%     suma_bledow_resubLoss = suma_bledow_resubLoss + blad;
%     cvtree = crossval(clknn);
%     blad = kfoldLoss(cvtree);
%     suma_bledow_kfoldLoss = suma_bledow_kfoldLoss + blad;
% 
% end
% resubLoss_1_sasiad = suma_bledow_resubLoss/NN
% kfoldLoss_1_sasiad = suma_bledow_kfoldLoss/NN
% 
% %Liczba sasiadow: k=3
% suma_bledow_resubLoss = 0;
% suma_bledow_crossval = 0;
% suma_bledow_kfoldLoss = 0;
% for i = 1:NN
%     data = dane;
%     data = data(randperm(N),:);
%     X = data(:, 1:7);
%     Y = data(:, 8);
%     clknn = fitcknn(X, Y, 'NumNeighbors',3);
%     %clknn = fitcknn(X, Y, 'NumNeighbors',3, 'Distance', 'mahalanobis');
%     blad = resubLoss(clknn);
%     suma_bledow_resubLoss = suma_bledow_resubLoss + blad;
%     cvtree = crossval(clknn);
%     blad = kfoldLoss(cvtree);
%     suma_bledow_kfoldLoss = suma_bledow_kfoldLoss + blad;
% 
% end
% resubLoss_3_sasiadow = suma_bledow_resubLoss/NN
% kfoldLoss_3_sasiadow = suma_bledow_kfoldLoss/NN
% 
% %Liczba sasiadow: k=4
% suma_bledow_resubLoss = 0;
% suma_bledow_crossval = 0;
% suma_bledow_kfoldLoss = 0;
% for i = 1:NN
%     data = dane;
%     data = data(randperm(N),:);
%     X = data(:, 1:7);
%     Y = data(:, 8);
%     clknn = fitcknn(X, Y, 'NumNeighbors',4);
%     %clknn = fitcknn(X, Y, 'NumNeighbors',4, 'Distance', 'mahalanobis');
%     blad = resubLoss(clknn);
%     suma_bledow_resubLoss = suma_bledow_resubLoss + blad;
%     cvtree = crossval(clknn);
%     blad = kfoldLoss(cvtree);
%     suma_bledow_kfoldLoss = suma_bledow_kfoldLoss + blad;
% 
% end
% resubLoss_4_sasiadow = suma_bledow_resubLoss/NN
% kfoldLoss_4_sasiadow = suma_bledow_kfoldLoss/NN


%Mahalanobisa

%Liczba sasiadow: k=1
suma_bledow_resubLoss = 0;
suma_bledow_crossval = 0;
suma_bledow_kfoldLoss = 0;
for i = 1:NN
    data = dane;
    data = data(randperm(N),:);
    X = data(:, 1:7);
    Y = data(:, 8);
    clknn = fitcknn(X, Y, 'NumNeighbors',1, 'Distance', 'mahalanobis');
    blad = resubLoss(clknn);
    suma_bledow_resubLoss = suma_bledow_resubLoss + blad;
    cvtree = crossval(clknn);
    blad = kfoldLoss(cvtree);
    suma_bledow_kfoldLoss = suma_bledow_kfoldLoss + blad;

end
resubLoss_1_sasiad_mahalanobis = suma_bledow_resubLoss/NN
kfoldLoss_1_sasiad_mahalanobis = suma_bledow_kfoldLoss/NN

%Liczba sasiadow: k=3
suma_bledow_resubLoss = 0;
suma_bledow_crossval = 0;
suma_bledow_kfoldLoss = 0;
for i = 1:NN
    data = dane;
    data = data(randperm(N),:);
    X = data(:, 1:7);
    Y = data(:, 8);
    clknn = fitcknn(X, Y, 'NumNeighbors',3, 'Distance', 'mahalanobis');
    blad = resubLoss(clknn);
    suma_bledow_resubLoss = suma_bledow_resubLoss + blad;
    cvtree = crossval(clknn);
    blad = kfoldLoss(cvtree);
    suma_bledow_kfoldLoss = suma_bledow_kfoldLoss + blad;

end
resubLoss_3_sasiadow_mahalanobis = suma_bledow_resubLoss/NN
kfoldLoss_3_sasiadow_mahalanobis = suma_bledow_kfoldLoss/NN

%Liczba sasiadow: k=4
suma_bledow_resubLoss = 0;
suma_bledow_crossval = 0;
suma_bledow_kfoldLoss = 0;
for i = 1:NN
    data = dane;
    data = data(randperm(N),:);
    X = data(:, 1:7);
    Y = data(:, 8);
    clknn = fitcknn(X, Y, 'NumNeighbors',4, 'Distance', 'mahalanobis');
    blad = resubLoss(clknn);
    suma_bledow_resubLoss = suma_bledow_resubLoss + blad;
    cvtree = crossval(clknn);
    blad = kfoldLoss(cvtree);
    suma_bledow_kfoldLoss = suma_bledow_kfoldLoss + blad;

end
resubLoss_4_sasiadow_mahalanobis = suma_bledow_resubLoss/NN
kfoldLoss_4_sasiadow_mahalanobis = suma_bledow_kfoldLoss/NN