clear
clc

%Warunki poczatkowe i warunki symulacji
alpha = pi/4;
g = 10;
x0 = 0;
y0 = 0;
v0 = 20;
v0x = v0 * cos(alpha);
v0y = v0 * sin(alpha);

dt = 0.1;
tmax = 3;

%Warunek poczatkowy
W0 = [0; 0; v0x; v0y];

A = [1 0 dt 0; 0 1 0 dt; 0 0 1 0; 0 0 0 1];
B = [0; -1/2*dt^2*g; 0; -g*dt];
C = [1 0 0 0; 0 1 0 0];

%Zadanie 1
WynikX_SM = W0;
X = W0;
for t=0:dt:tmax
    X = A*X+B;
    WynikX_SM = [WynikX_SM X];
end


WynikY_SM = C * WynikX_SM;
plot(WynikY_SM(1,:), WynikY_SM(2,:),'blue');
hold on

%Zadanie 2
sigma = 3;
sigma_o = 1;

X = W0;
WynikX_ST = W0;
WynikY_O = C * W0;

for t=0:dt:tmax
    E1 = randn;
    E2 = randn;
    W = [0.5*dt^2*E1; 0.5*dt^2*E2; E1*dt; E2*dt] * sigma;
    X = A*X + B + W;
    WynikX_ST = [WynikX_ST X];
    E3 = randn;
    E4 = randn;
    V = [E3; E4] * sigma_o;
    Y = C * X + V;
    WynikY_O = [WynikY_O Y];
end
WynikY_ST = C * WynikX_ST;
plot(WynikY_ST(1,:), WynikY_ST(2,:), 'red');
hold on
plot(WynikY_O(1,:), WynikY_O(2,:), 'blue');
scatter(WynikY_O(1,:), WynikY_O(2,:))

%Zadanie 3

R = [1 0; 0 1] * sigma_o^2;
Q = [dt^4/4 0 dt^3/2 0; 0 dt^4/4 0 dt^3/2; dt^3/2 0 dt^2 0; 0 dt^3/2 0 dt^2] * sigma^2;
WynikY_E = C*W0;
X_E = W0;
P = Q;
for i=2:length(WynikY_ST)
    X_E = A*X_E + B;
    P_til = A*P*A' + Q;
    K = P_til * C' * inv(C*P_til*C' + R);
    X_E = X_E + K*(WynikY_ST(:,i) - C*X_E);
    P = (eye(4)-K*C) * P_til;
    WynikY_E = [WynikY_E C*X_E];
end

plot(WynikY_E(1,:), WynikY_E(2,:), 'green')
