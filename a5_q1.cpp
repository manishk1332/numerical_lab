#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

double u0(double x) {
    if(x>(-1.0/3.0) && x<(1.0/3.0)) {
        return 1;
    }
    else return 0;
}

void solve(int n, int m, vector<double>& x, vector<double>& t) {
    vector<double> u(n+1);
    for(int i=0;i<=n;i++) {
        u[i] = u0(x[i]);
    }
    vector<double> v(n+1);

    while(m--) {
        for(int i=1;i<n;i++) {
            v[i] = 0.1*u[i+1]+0.9*u[i-1];
        }
        v[0] = 0.1*u[1]+0.9*u[n-1];
        v[n] = 0.1*u[1]+0.9*u[n-1];
        u.assign(v.begin(), v.end());
    }
    for(int i=0;i<=n;i++) {
        cout<<"u("<<x[i]<<", 4) = "<<u[i]<<'\n';
    }
}

int main() {
    int n = 500;
    double a = -1.0;
    double b = 1.0;
    double dx = (b - a) / n;
    double dt = 0.8 * dx;
    int m = static_cast<int>(4 / dt);  // 500

    vector<double> x(n + 1), t(m + 1);

    for (int i = 0; i <= n; ++i) {
        x[i] = a + i * dx;
    }

    for (int i = 0; i <= m; ++i) {
        t[i] = i * dt;
    }
    solve(n, m, x, t);

    n = 5000;
    a = -1.0;
    b = 1.0;
    dx = (b - a) / n;
    dt = 0.8 * dx;
    m = static_cast<int>(4 / dt);

    vector<double> x2(n + 1), t2(m + 1);

    for (int i = 0; i <= n; ++i) {
        x2[i] = a + i * dx;
    }

    for (int i = 0; i <= m; ++i) {
        t2[i] = i * dt;
    }

    //solve(n,m,x2,t2);
    return 0;

}