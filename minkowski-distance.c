#include <stdio.h>
#include <math.h>

typedef struct point {
        float x,
              y; 
} Point;

void readPoint(Point *p) {

     printf("Abs=");
     scanf("%f", &p->x); 
     printf("Ord=");
     scanf("%f", &p->y); 
};

/*
    p1 - first point
    p2 - second point
    n  - order distance
    returns the distance between p1 and p2 
 */

float minkowski_distance_procedural(Point p1, Point p2, int n) {


      return (abs(p2.x - p1.x) + abs(p2.y - p1.y))^n/1/n
};

int main(void) {

    Point p1, p2;

    readPoint(&p1); 
    readPoint(&p2); 
    printf("Minkowski Distance = %f",minkowski_distance_procedural(p1, p2, 2));
 
 return(0);
};