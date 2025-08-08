#include<stdio.h>
#include<stdlib.h>
#include <time.h>

 int main () {
// initialize ramndom number generator 
srand(time (0)) ;
// generate random number betwenn 1 and 100 
 int randomnumber = (rand () % 100) +1 ;
int no_of_guesses = 0;
int guessed_number ;
 // print the random number 
 //printf(" random number : %d \n ", random number );

do
{
    printf("guess the number ");
    scanf("%d", &guessed_number);
    if(guessed_number>randomnumber){
      printf("lower number please \n ");
    }

 else if
 (guessed_number<randomnumber){
      printf("higher  number please \n ");
    }
 else{
    printf("congrats \n");
 }
no_of_guesses++;

} while (guessed_number !=  randomnumber);
printf("you guessed the number in %d guesses", no_of_guesses);

    return 0;

 }