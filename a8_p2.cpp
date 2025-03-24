#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

const int n = 50;
const double a = 0.0;
const double b = 1.0;
const double dx = (b - a) / n;
const double F = 0.9;
const double dt = F*0.5*(dx*dx);
const double T = 200;
const double pi = M_PI;

int main() {
    vector<double> X(n + 1);
    for (int i = 0; i <= n; ++i) {
        X[i] = a + i * dx;
    }

    vector<vector<double>> u(n + 1, vector<double>(T+1, 0.0)); 
    for(int i=0;i<=n;i++) {
        if(X[i]<0.5) u[i][0] = 2*X[i];
        else u[i][0] = 2*(1-X[i]);
    }
    for(int t=0;t<T;t++) {
        for(int x=1;x<n;x++) {
            u[x][t+1] = u[x][t]+(dt/(dx*dx))*(u[x+1][t] - 2*u[x][t] + u[x-1][t]);
        }
    }
    cout<<"Time step 50   100   200\n";
    for(int x=0;x<=n;x++) {
        cout<<"at x="<<X[x]<<"  "<<u[x][50]<<"  "<<u[x][100]<<"  "<<u[x][200]<<"\n";
    }
    return 0;
}