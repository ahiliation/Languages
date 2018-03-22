#include <stdio.h>
int main() {
  void test(int *);
  int n = 14;
  printf("%d\n", n);
  test(&n);
  printf("%d\n", n);
} //end main
// before calling test
// after return from test

void test(int *a) {
  *a = *a + 5;
  printf("%d\n", *a);
} //end test
// within test
