#include <bits/stdc++.h>
using namespace std;
void solve() {

    int n; int X;
    cin >> n; cin >> X;
    int arr[n];

    for (int i = 0; i<n; i++) {
        cin >> arr[i];
    }

    sort(arr, arr + n);

    int p1 = 0; int p2 = n-1;
    long long sum = 0;
    long long points = 0;
    long long opt[n];
    int i = -1;

    do {
        if (arr[p2]+sum>X) {
            sum+=arr[p2];
            i++;
            opt[i]=arr[p2];
            p2--;
        } else {
            sum+=arr[p1];
            i++;
            opt[i]=arr[p1];
            p1++;
        }

        if(sum>=X) {
            sum-=X;
            points += opt[i];
        }

    } while (p1!=p2+1);

    cout << points << '\n';
    
    for (int i = 0; i<n; i++) {
        cout << opt[i] << ' ';
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