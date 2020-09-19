# SVM primal model
param n; #dimensio
param m; #n. dades
param A{1..m, 1..n+1};
param sigma;
param nu;
var w{1..n};
var s{1..m} >= 0;
var gamma;

minimize f: 0.5*(sum{i in 1..n} w[i]*w[i]) + nu*sum{j in 1..m} s[j];
subject to h{i in 1..m}: A[i,n+1]*((sum{j in 1..n}w[j]*A[i,j])+gamma)+s[i] >= 1;





