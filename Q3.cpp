#include <bits/stdc++.h>

using namespace std;
#define int long long
#define float double
float phi(float x,float y,float w)
{
    return 2*x*x*exp(x)+3*w/x-3*y/(x*x);
}
float f(float x,float y,float w)
{
    return w;
}
signed main()
{
    vector <float> u_val(11);
    vector <float> w_val(11);
    u_val[0]=0;
    w_val[0]=0;
    float x=1;
    float u=0;
    float w=0;
    float h=0.1;
    for(int i=0;i<10;i++)
    {
        float k1=h*f(x,u,w);
        float l1=h*phi(x,u,w);
        float k2=h*f(x+h/2,u+k1/2,w+l1/2);
        float l2=h*phi(x+h/2,u+k1/2,w+l1/2);
        float k3=h*f(x+h/2,u+k2/2,w+l2/2);
        float l3=h*phi(x+h/2,u+k2/2,w+l2/2);
        float k4=h*f(x+h,u+k3,w+l3);
        float l4=h*phi(x+h,u+k3,w+l3);
        x+=h;
        u+=(k1+2*k2+2*k3+k4)/6;
        w+=(l1+2*l2+2*l3+l4)/6;
        u_val[i+1]=u;
        w_val[i+1]=w;
    }
    vector <float> v_val(11);
    vector <float> z_val(11);
    v_val[0]=0;
    z_val[0]=1;
    x=1;
    u=0;
    w=1;
    for(int i=0;i<10;i++)
    {
        float k1=h*f(x,u,w);
        float l1=h*phi(x,u,w);
        float k2=h*f(x+h/2,u+k1/2,w+l1/2);
        float l2=h*phi(x+h/2,u+k1/2,w+l1/2);
        float k3=h*f(x+h/2,u+k2/2,w+l2/2);
        float l3=h*phi(x+h/2,u+k2/2,w+l2/2);
        float k4=h*f(x+h,u+k3,w+l3);
        float l4=h*phi(x+h,u+k3,w+l3);
        x+=h;
        u+=(k1+2*k2+2*k3+k4)/6;
        w+=(l1+2*l2+2*l3+l4)/6;
        v_val[i+1]=u;
        z_val[i+1]=w;
    }
    
    float lambda=(4*exp(2)-v_val[10])/(u_val[10]-v_val[10]);
    for(int i=0;i<11;i++)
    {   
        x=1+i*h;
        float act=2*x*exp(x)*(x-1);
        cout<<"Evaluated: "<<lambda*u_val[i]+(1-lambda)*v_val[i]<<" Actual: "<<act<<'\n';
    }

}