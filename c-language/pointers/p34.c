#include<stdio.h>

main() {
  char *errorMessage;
  errorMessage = "Negative argument to square root\n";
  printf("%c\n", errorMessage[1]);
  printf("%s",errorMessage);
}
