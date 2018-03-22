#include <stdio.h>
int main() {
  void test(int val[], int max);
  int j, list[5];

  for (j = 0; j < 5; j++)
    {
    list[j] = j;
    printf("list[j] is  %d and j is %d \n",list[j],j);
    }
  test(list, 5);
  for (j = 0; j < 5; j++) printf("%d ", list[j]);
  printf("\n");
} //end main

void test(int val[], int max) {
  // add 25 to each of val[0] to val[max - 1]
  int j;
  for (j = 0; j < max; j++) val[j] += 25;
} //end test
