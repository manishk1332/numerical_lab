#include <bits/stdc++.h>

using namespace std;
#define int long long
#define float double
vector<float> pqr(float x)
{
    vector<float> ans(3);
    ans[0]=exp(x);
    ans[1]=-x;
    ans[2]=(-x*x+2*x-3)*exp(-x)-x+2;
    return ans;
}
float y(float x)
{
    return (x-1)*exp(-x);
}

void out(vector <vector<double>>v)
{
     for (auto i : v)
    {
        for(auto j:i)
            cout<<j<<' ';
        cout<<'\n';
    }
}
vector<vector<double>> drop_col(vector<vector<double>> temp,int m)
{
    auto v=temp;
    for(int i=0;i<v.size();i++)
    {
        v[i].erase(v[i].begin()+m);
    }
    return v;
}
vector<vector<double>> drop_row(vector<vector<double>> temp,int m)
{
    auto v=temp;
    v.erase(v.begin()+m);
    return v;
}
double deter(vector<vector <double >>v)
{
    double val=0;
    if(v.size()==1)
        return v[0][0];
    else
    {
        int index=1;
        for(int i=0;i<v.size();i++)
        {
            auto temp=drop_col(v,i);
            temp=drop_row(temp,0);
            val+=(v[0][i]*index*deter(temp));
            index*=-1;
        }
        
    }
    return val;
}
vector <vector<double>> inv(vector <vector<double>> v)
{
    int n=v.size();
    double det=deter(v);
    vector <vector<double>> temp;
    temp.assign(n,vector<double>(n,0));
    int index=1;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            vector <vector<double>> temp2=drop_row(v,i);
            temp2=drop_col(temp2,j);
            temp[j][i]=index*deter(temp2)/det;
            index*=-1;
        }
        index*=-1;
    }
    return temp;
}
signed main()
{
    vector<vector<float>> A;
    vector<float> B;
    A.assign(9,vector<float>(9,0));
    B.assign(9,0);
    float h=0.1;
    vector <float> y_val(11);
    y_val[0]=-1;
    y_val[10]=0;
    for(int i=0;i<9;i++)
    {
        float x=(i+1)*h;
        auto coef=pqr(x);
        A[i][i]=-2+(h*h)*coef[1];
        if(i>0)
            A[i][i-1]=1-(h/2)*coef[0];
        if(i<8)
            A[i][i+1]=1+h*coef[0]/2;
        B[i]=h*h*coef[2];
        if(i==0)
            B[i]-=(1-(h/2)*coef[0])*y_val[0];
        if(i==8)
            B[i]-=(1+(h/2)*coef[0])*y_val[10];
    }
    
    A=inv(A);
    for(int i=0;i<9;i++)
    {
        for(int j=0;j<9;j++)
            cout<<A[i][j]<<' ';
        cout<<'\n';
    }
    for(int i=0;i<9;i++)
    {
        for(int j=0;j<9;j++)
        {
            y_val[i+1]+=A[i][j]*B[j];
        }
    }
    
    for(int i=0;i<11;i++)
        cout<<"Evaluated: "<<y_val[i]<<" Actual: "<<y(0+i*h)<<'\n';

}