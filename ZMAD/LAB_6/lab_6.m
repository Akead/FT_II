clear
clc

%dane = importdata('wifi_localization.txt');
dane_h = importdata('housing.txt');

% N = length(dane);
% N_tr = 1600;
% N_te = N - N_tr;
% res = ones(N_te,1);



% %-----------------------------------------------------------------
% 
% %ZADANIE 1
% dane = dane(randperm(N),:);
% X_tr = dane(1:N_tr, 1:7);
% Y_tr = dane(1:N_tr, 8);
% X_te = dane(N_tr+1:end, 1:7);
% Y_te = dane(N_tr+1:end, 8);
% clknn = fitctree(X_tr, Y_tr, 'Prune','off');
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
% saveas(gcf, 'lipior_6_11.png')
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
% saveas(gcf, 'lipior_6_12.png')
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
% saveas(gcf, 'lipior_6_13.png')
% 
% view(clknn, 'mode','graph')



% %----------------------------------------------------------------
% 
% % ZADANIE 2
% 
% NN = 200;
% nn = 8;
% bledy = [];
% for ll = 1:nn
%     suma_bledow = 0;
%     for i = 1:NN
%         data = dane;
%         data = data(randperm(N),:);
%         X_tr = data(1:N_tr, 1:7);
%         Y_tr = data(1:N_tr, 8);
%         X_te = data(N_tr+1:end, 1:7);
%         Y_te = data(N_tr+1:end, 8);
%         clknn = fitctree(X_tr, Y_tr, 'Prune','off');
%         clknn = prune(clknn, 'Level',ll);
%         y_validated = predict(clknn, X_te);
%         blad = res(Y_te~=y_validated);
%         blad = length(blad);
%         suma_bledow = suma_bledow + blad;
%     end
%     blad_sredni = suma_bledow/NN/N_te;
%     bledy(end+1) = blad_sredni;
%     view(clknn, 'mode','graph') 
% end
% 
% plot(1:nn,bledy, 1:nn, bledy, 'ro')
% 
% %----------------------------------------------------------------

% %----------------------------------------------------------------
% 
% % ZADANIE 3

N = length(dane_h);
N_tr = 450;
N_te = N - N_tr;
res = ones(N_te,1);
dane_h = dane_h(randperm(N),:);

X = dane_h(:,1:13);
Y = dane_h(:,14);

tree = fitrtree(X,Y);
y_validated = predict(tree, X);
display('sredni blad:')
sqrt(mean((y_validated-Y).^2))/mean(Y)
blad = (y_validated - Y)./Y;


tree = fitrtree(X,Y);
tree = prune(tree, 'Level',10);
y_validated = predict(tree, X);
display('sredni blad po przycieciu:')
sqrt(mean((y_validated-Y).^2))/mean(Y)
blad_2 = (y_validated - Y)./Y;
plot(blad, 'Color','Blue')
hold on
plot(blad_2, 'Color','Red')

