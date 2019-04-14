# Writeup 7 - Binaries I

Name: Tuan Le
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Tuan Le

## Assignment Writeup

### Part 1 (90 Pts)

int main(int a, int b) {
  printf("%d\n", a);
  printf("%d\n", b);
  a ^= b;
  b ^= a;
  a ^= b;
  printf("%d\n", a);
  printf("%d\n", b);
  return 0;
}

### Part 2 (10 Pts)

This program takes in two numbers as input in two distinct variables. The program achieves the purpose of swapping the values of the variables without using a temporary variable.
