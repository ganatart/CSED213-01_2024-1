#include <bits/stdc++.h>

using namespace std;

const long long int mod = 1e9 + 7;

struct mat{
    long long int arr[3][3];

    mat(bool I){
        if(I){
            for(int r = 0; r < 3; r++)
            for(int c = 0; c < 3; c++) arr[r][c] = r == c;
        }else{
            for(int r = 0; r < 3; r++)
            for(int c = 0; c < 3; c++) arr[r][c] = 1;
            arr[1][1] = arr[1][2] = arr[2][0] = arr[2][2] = 0;
        }
    }
};

mat operator *(mat m1, mat m2){
    mat res(true);
    for(int i = 0; i < 3; i++)
    for(int j = 0; j < 3; j++) res.arr[i][j] = 0;

    for(int i = 0; i < 3; i++)
    for(int j = 0; j < 3; j++)
    for(int k = 0; k < 3; k++) res.arr[i][j] = (res.arr[i][j] + m1.arr[i][k] * m2.arr[k][j]) % mod;
    return res;
}

mat pow(mat m, long long int a){
    if(a == 0) return mat(true);
    mat res = pow(m, a / 2);
    res = res * res;
    if(a % 2 == 1) res = res * m;
    return res;
}

int main(){
    long long int N;
    cin >> N;

    mat m(false);
    m = pow(m, N + 1);
    cout << m.arr[0][0];
}