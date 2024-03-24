#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


int coordinates[2];

void drawMap(int height, int width, int playerPos[2]){
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            if(j == playerPos[0] && i == playerPos[1]){
                printf("█ ");
            }
            else{
                printf("# ");
            }
        }
        printf("\n");
    } // Refresh the screen to show the changes
}

void playerAction(char action){
    switch(action) {
        case 'a':
        case 'A':
            coordinates[0]--;
            break;
        case 'w':
        case 'W':
            coordinates[1]--;
            break;
        case 's':
        case 'S':
            coordinates[1]++;
            break;
        case 'd':
        case 'D':
            coordinates[0]++;
            break;
    }
}

int main(){
    char action;

    coordinates[0] = 5;
    coordinates[1] = 6;

    while(true){
        printf("\033[2J\033[H");
        drawMap(10, 20, coordinates);
        printf("Enter action:\n");
        scanf("%2c", &action);
        playerAction(action);
    }
    return 0;
}
