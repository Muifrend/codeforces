#include <bits/stdc++.h>
using namespace std;

void solve() {

    int numbers[3];

    for (int i = 0; i < 3; i++) {
        cin >> numbers[i];
    }
    
    int n = numbers[0];
    int prefix[n];
    int y = 0;

    for (int i = 0; i < numbers[0] ; i++) {
        if (n - i <= numbers[1]) {
            y += 1;
            prefix[i] = y;
        } else {
            prefix[i] = n - i;
        }
        cout << prefix[i] << ' ';
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        solve();
        cout << '\n';
    }
    return 0;
}