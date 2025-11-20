#include <bits/stdc++.h>
using namespace std;
void solve() {
 
    string n; int l; int k;
    cin >> n; cin >> l; cin >> k;
    int len = n.length();
 
    vector<string> arr;
 
    do {
        arr.push_back(n);
    } while (next_permutation(n.begin(), n.end()));
 
    string one = arr[l-1];
    string two = arr[k-1];
 
    int a = 0;
 
    for (int i = 0; i<len; i++) {
        if(one[i]==two[i]){
            a++;
        }
    }
 
    cout << a << 'A' << len-a << 'B';
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