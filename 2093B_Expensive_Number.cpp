#include <bits/stdc++.h>
using namespace std;

void solve() {  
    int counter = 0;
    string number; 
    cin >> number;
    bool flag = true;
    bool flag2 = false;
    for (int i = number.size() - 1; i >= 0; i--) {
        char digit = number[i];

        if (flag && digit == '0') {
            counter++;
        } else {
            flag = false;
        }

        if (!flag && digit != '0') {
            if (flag2) counter++;
            flag2 = true;
        }
    }
    cout << counter <<'\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}