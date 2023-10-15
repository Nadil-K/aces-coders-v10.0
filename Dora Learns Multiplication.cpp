// Dora Learns Multiplication

#include <iostream>
#include <vector>
#include <cmath>
#include <complex>
using namespace std;

typedef complex<double> base;

void fft(vector<base> &a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; ++i) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1)
            j ^= bit;
        j ^= bit;
        if (i < j)
            swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        double ang = 2 * M_PI / len * (invert ? -1 : 1);
        base wlen(cos(ang), sin(ang));
        for (int i = 0; i < n; i += len) {
            base w(1);
            for (int j = 0; j < len / 2; ++j) {
                base u = a[i+j], v = a[i+j+len/2] * w;
                a[i+j] = u + v;
                a[i+j+len/2] = u - v;
                w *= wlen;
            }
        }
    }

    if (invert)
        for (int i = 0; i < n; ++i)
            a[i] /= n;
}

vector<int> multiply(const vector<int> &a, const vector<int> &b) {
    vector<base> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    int n = 1;
    while (n < max(a.size(), b.size()))
        n <<= 1;
    n <<= 1;
    fa.resize(n); fb.resize(n);

    fft(fa, false); fft(fb, false);
    for (int i = 0; i < n; ++i)
        fa[i] *= fb[i];
    fft(fa, true);

    vector<int> result(n);
    for (int i = 0; i < n; ++i)
        result[i] = int(fa[i].real() + 0.5);
    return result;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        string s1, s2;
        cin >> s1 >> s2;
        vector<int> a(s1.size()), b(s2.size());
        for (int i = 0; i < s1.size(); ++i)
            a[i] = s1[s1.size() - 1 - i] - '0';
        for (int i = 0; i < s2.size(); ++i)
            b[i] = s2[s2.size() - 1 - i] - '0';

        vector<int> res = multiply(a, b);
        int carry = 0;
        for (int i = 0; i < res.size(); ++i) {
            res[i] += carry;
            carry = res[i] / 10;
            res[i] %= 10;
        }
        int idx = res.size() - 1;
        while (idx > 0 && res[idx] == 0)
            idx--;
        for (int i = idx; i >= 0; --i)
            cout << res[i];
        cout << "\n";
    }
    return 0;
}
