#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

const int n = 200;
const double a = -1.0;
const double b = 1.0;
const double dx = (b - a) / n;
const double T = 0.5;

double spectral_rad(int t, const vector<vector<double>>& u, const vector<vector<double>>& rho) {
    double max_val = -1.0;
    for (int i = 0; i <= n; ++i) {
        max_val = max(abs(u[i][t]), max_val);
    }
    return max_val;
}

int main() {
    vector<double> x(n + 1);
    for (int i = 0; i <= n; ++i) {
        x[i] = a + i * dx;
    }

    vector<vector<double>> u(n + 1, vector<double>(1002, 0.0)); 
    vector<vector<double>> rho(n + 1, vector<double>(1002, 1.0)); 

    for (int i = 0; i <= n; ++i) {
        if (x[i] < 0) {
            u[i][0] = 2.0;
        } else {
            u[i][0] = -2.0;
        }
    }

    vector<double> time;
    double time_val = 0.0;
    time.push_back(time_val);

    for (int t = 0; t < 1001; ++t) {
        double dt = (0.9 * dx) / spectral_rad(t, u, rho);
        time_val += dt;

        if (time_val > T) {
            break;
        }

        time.push_back(time[time.size() - 1] + dt);

        for (int i = 0; i <= n; ++i) {
            int l = i - 1;
            int r = i + 1;

            if (l == -1) l = 0;
            if (r == n + 1) r = n;

            rho[i][t + 1] = (rho[r][t] + rho[l][t]) / 2.0 - dt * (rho[r][t] * u[r][t] - rho[l][t] * u[l][t]) / (2.0 * dx);
            u[i][t + 1] = (rho[r][t] * u[r][t] + rho[l][t] * u[l][t]) / (2.0 * rho[i][t + 1]) - dt * (rho[r][t] * pow(u[r][t], 2) - (rho[l][t] * pow(u[l][t], 2))) / (2.0 * dx * rho[i][t + 1]);
        }
    }

    cout << "Final time: " << time_val << endl;
    for(int t=0;t<time.size();t++) {
        for(int j=0;j<=n;j++) {
            std::cout<<"At time t="<<time[t]<<", x="<<x[j]<<" u="<<u[j][t]<<" and rho="<<rho[j][t]<<'\n';
        }
    }

    return 0;
}
