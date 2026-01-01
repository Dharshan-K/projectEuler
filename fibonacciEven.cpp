#include <iostream>
#include <vector>

long long fibonacci(long long n, std::vector<long long>& memo, long long sum) {
    if (n <= 1) {
        return n;
    }
    if (memo[n] != -1) {        
        return memo[n];          
    }
    memo[n] = fibonacci(n - 1, memo, sum) + fibonacci(n - 2, memo, sum);
    return memo[n];
}

int main() {
    long long n = 45;
    std::vector<long long> memo(n + 1,-1);
    long long sum = 0;
    long long target = 4000000;

    std::cout << "Fibonacci(" << n << ") = " << fibonacci(n, memo, sum) << "\n";
    for (int i = 0; i < memo.size(); i++){
        if(memo [i] < target && memo[i] % 2 == 0){
            // std::cout << memo[i] << "\n";
            sum = sum + memo[i];
        }
    }
    std::cout << "Sum is: " << sum;
    return 0;
}

