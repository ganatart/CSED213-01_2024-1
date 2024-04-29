#include <bits/stdc++.h>

using namespace std;

const int MX = 1005;
const long long int mod = 1e9 + 7;

long long int dp[MX][MX], pow2[MX];

int main(){
    cin.tie(nullptr), ios::sync_with_stdio(false);

    pow2[0] = 1;
    for(int i = 1; i < MX; i++) pow2[i] = (pow2[i - 1] * 2) % mod;

    int N;
    cin >> N;

    dp[0][0] = 1;

    for(int num = 1; num <= N; num++){
        for(int pos = 1; pos <= N; pos++){
            for(int prv = max(0, pos - 3); prv < pos; prv++){
                dp[num][pos] = (dp[num][pos] + dp[num - 1][prv]) % mod;
            }
        }
    }

    for(int num = 0; num <= N; num++){
        for(int prv = max(0, N - 2); prv <= N; prv++){
            dp[num][N + 1] = (dp[num][N + 1] + dp[num][prv]) % mod;
        }
    }

    long long int ans = 0;
    for(int num = 0; num <= N; num++){
        ans = (ans + dp[num][N + 1] * pow2[N - num] % mod) % mod;
    }

    cout << ans;
}