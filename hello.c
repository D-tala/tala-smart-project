#include <stdio.h>
#include <stdbool.h>
#include <math.h>
int main()
{  
     int a,b,product; 
    bool ismathguru= true;
    if(ismathguru){
        printf("You are good to go\n");

printf("\n Enter a:");
scanf("%d", &a);
printf("\n Enter b:");
scanf("%d", &b);
product= a*b;
printf("\n The product of a and b is = %d", product);   

    
    int booknumber;
    bool isstudent= true;
    if(isstudent){
        printf("\n You are allowed to inquire for a book");
        printf("\n Lets go to the Library........");
    printf("\n Enter the book number from (1-4) :");
    scanf("%d", & booknumber);
    switch(booknumber){
        case 1:1;
        printf("The Samaritan");
        break;
        case 2:2;
        printf("Dolls House");
        break;
        case 3:3;
        printf("Blosssoms");
        break;
        case 4:4;
        printf("Bembea");
        break;
        default:
        printf("Enter a valid booknumber from 1-4 :");

    }
    printf("\n Do you want to ask for another book? (y/n): ");
    char choice;
    scanf(" %c", &choice);
}
    else if(!isstudent){
        printf("\n You are not allowed to ask for a book");
    }
    
    else{
        printf("wrong input");
    }
    }
    else if(!ismathguru){
        printf("\n You are not a math guru😪😪😪");
    }
    else{
        printf("wrong input");
    }
   
    return 0;
}

