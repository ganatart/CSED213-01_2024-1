#include <bits/stdc++.h>

using namespace std;

const int MX = 2e5 + 5;
const long long int mod = 1e9 + 7;

int N, K, arr[MX];
long long int dp[MX];

int main(){
    cin.tie(nullptr), ios::sync_with_stdio(false);
    cin >> N >> K;
    for(int i = 1; i <= K; i++){
        int x;
        cin >> x;
        arr[x] = 1;
    }

    dp[0] = 1;
    dp[1] = dp[0];
    if(arr[1]) dp[1] = 0;
    dp[2] = dp[0] + dp[1];
    if(arr[2]) dp[2] = 0;

    for(int i = 3; i <= N + 1; i++){
        dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % mod;
        if(arr[i]) dp[i] = 0;
    }

    cout << dp[N + 1];
}