# SVM dual model amb Gaussian Kernel
param n; #dimensio
param m; #n. dades
param A{1..m, 1..n+1};
param nu;
param sigma;
var lambda{1..m} >=0, <= nu;

maximize f: sum{i in 1..m} lambda[i] - 1/2*(sum{i in 1..m, j in 1..m} 
lambda[i]*A[i,n+1]*lambda[j]*A[j,n+1]*exp(-1/(2*sigma)*(sum{k in 1..n}(A[i,k]-A[j,k])^2)));

subject to h: sum{i in 1..m}lambda[i]*A[i,n+1] = 0;


