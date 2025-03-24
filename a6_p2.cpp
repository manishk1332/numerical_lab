#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

const double g = 9.81;
const int n = 500;
const double a = 0;
const double b = 5;
const double dx = (b - a) / n;
const double T = 1.0;

std::vector<double> x(n + 1);

double spectral_rad(int t, const std::vector<std::vector<double>>& u, const std::vector<std::vector<double>>& h) {
    double max_val = -1;
    for (int i = 0; i <= n; ++i) {
        double lb1 = std::abs(u[i][t]+std::sqrt(g * h[i][t]));
        double lb2 = std::abs(u[i][t]-std::sqrt(g * h[i][t]));
        double temp_max = std::max(lb1, lb1);
        max_val = std::max(temp_max, max_val);
    }
    //std::cout<<max_val<<" ";
    return max_val;
}

int main() {
    std::vector<std::vector<double>> u(n + 1, std::vector<double>(1001, 0));
    std::vector<std::vector<double>> h(n + 1, std::vector<double>(1001, 0));

    // Set initial conditions for h(x, 0) and u(x, 0)
    for (int i = 0; i <= n; ++i) {
        x[i] = a + i * dx;
        if(x[i]<2.5) h[i][0] = 2;
        else h[i][0] = 1;
    }

    std::vector<double> time = {0};
    double time_val = 0;

    for (int t = 0; t <= 1000; ++t) {
        double dt = (0.9 * dx) / spectral_rad(t, u, h);
        //std::cout<<dt<<" ";
        time_val += dt;
        
        if (time_val > T) {
            break;
        }
        
        time.push_back(time.back() + dt);

        for (int i = 0; i <= n; ++i) {
            int l = i - 1;
            int r = i + 1;
            if (l == -1) l = 0;
            if (r == n + 1) r = n;

            h[i][t + 1] = (h[r][t] + h[l][t]) / 2 - dt * (h[r][t] * u[r][t] - h[l][t] * u[l][t]) / (2 * dx);
            u[i][t + 1] = (h[r][t] * u[r][t] + h[l][t] * u[l][t]) / (2 * h[i][t + 1]) - 
                dt * (h[r][t] * std::pow(u[r][t], 2) + 0.5 * g * std::pow(h[r][t], 2) -
                (h[l][t] * std::pow(u[l][t], 2) + 0.5 * g * std::pow(h[l][t], 2))) / (2 * dx * h[i][t + 1]);
        }
    }
    
    for(int t=0;t<time.size();t++) {
        for(int j=0;j<=n;j++) {
            std::cout<<"At time t="<<time[t]<<", x="<<x[j]<<" u="<<u[j][t]<<" and h="<<h[j][t]<<'\n';
        }
    }

    return 0;
}