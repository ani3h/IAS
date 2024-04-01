#include <stdio.h>
#include<math.h>

int Factorial(int n)
{
    int fact = 1;

    for(;n != 1; n--)
    {
        fact *= n;    
    }
    return fact;
}

int Permutation(int n, int m)
{
    return Factorial(n)/Factorial(n-m);
}

int main()
{
    int n = 10;
    int r = 2;

    int comb = Permutation(n,r)/Factorial(r);

    printf("%d", comb);

    return 0;
}

// Program to Find the Comination of a given number 'n', in 'r' ways.