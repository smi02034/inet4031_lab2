#include <stdio.h>
 
int main() {              
    int a = 2;
    int b = 2;
    int c = a + b;
              
    printf("C says: Hello, World!\n");
    printf("%d + %d = %d\n",a,b,c);
            
    // I chose to do an array of char pointers because it made the
    // array easier to print.
    char* listOfUsers[] = {"User1", "User2", "User3"};

    for(int i = 0; i < 3; i++) {
        printf("%s\n", listOfUsers[i]);
    }

    return 0;
}
