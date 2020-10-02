#include <bits/stdc++.h>
using namespace std;

string add (string a, string &b) {
    // make sure string 'a' is never greater than 'b'
    if (a.size() > b.size()) 
        swap(a, b); 
  
    string str = ""; 
  
    // calculate length of both string 
    int n1 = a.size(), n2 = b.size(); 
  
    // Reverse both of strings 
    reverse(a.begin(), a.end()); 
    reverse(b.begin(), b.end()); 
  
    int carry = 0; 
    for (int i = 0; i < n1; ++i) { 
        int num1 = a[i] - '0';
        int num2 = b[i] - '0';
        
        int sum = num1 + num2 + carry;
        char ch = (sum % 10 + '0');
        str += ch;
        
        carry = sum/10; 
    } 
  
    // Add remaining digits of larger number 
    for (int i = n1; i < n2; ++i) {
        int num = b[i] - '0';
        int sum = num + carry;
        
        char ch = sum%10 + '0';
        str += ch; 
        carry = sum/10; 
    } 
  
    // Add remaining carry if any
    if (carry) 
        str.push_back(carry+'0'); 
  
    // reverse resultant string 
    reverse(str.begin(), str.end()); 
    
    return str; 
}

int main () {
    // storing input in string since input is large
    string a;
    cin >> a;
    for (int i = 0; i < 99; ++i) {
        string b;
        cin >> b;
        a = add (a, b);
    }
    
    for (int i = 0; i < 10; ++i) 
        cout << a[i];
    
    cout << endl;
    return 0;
}
