#include <bits/stdc++.h>

using namespace std;
#define int long long
#define float double
float phi(float x,float y,float w)
    {
        return (1-w*w)/y;
    }
float f(float x,float y,float w)
    {
        return w;
    }
float rk(float s,int temp)
{
     vector <float> u_val(6);
        vector <float> w_val(6);
        u_val[0]=1;
        w_val[0]=s;
        float x=0;
        float u=1;
        float w=s;
        float h=0.4;
        for(int i=0;i<5;i++)
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
        if(temp)
        {
            for(int i=0;i<6;i++)
            {  
                cout<<u_val[i]<<'\n';
            }
        }
        return u_val[5]-2;
}
signed main()
    {
       float err=1e-4;
       float s0=0;
       float s1=2;
       while(abs(rk(s1,0))>err)
        {
            float temp=s1;
            s1=s1-(s1-s0)*rk(s1,0)/(rk(s1,0)-rk(s0,0));
            s0=temp;
        }
        float temp=s1;
            s1=s1-(s1-s0)*rk(s1,0)/(rk(s1,0)-rk(s0,0));
            s0=temp;
        rk(s1,1);
    }