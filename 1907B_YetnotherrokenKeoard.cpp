#include <bits/stdc++.h>
using namespace std;

void solve() {
    string s;
    cin >> s;
    
    reverse(s.begin(),s.end());

    int B = 0;
    int b = 0;
    string out;
    out.reserve(s.size());

    for (char c : s) {
        if (isupper(c)) {
            if (c == 'B') {
                B++;
            } else if (B > 0) {
                B--;
            } else {
                out.push_back(c);
            }
        } else {
            if (c == 'b') {
                b++;
            } else if (b > 0) {
                b--;
            } else {
                out.push_back(c);
            }
        } 
    }
    reverse(out.begin(),out.end());
    cout << out;
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