/*
 * Name: Tuan Le
 * Section: 0201
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Tuan Le
 */

/* your code goes here */

#include <stdio.h>

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
  
