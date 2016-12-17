 
$fn = 40;
 
difference () {
    union () {
        cube ( size = [32,4,17]);
        translate ([0,-5,15]) rotate ([0,90,0]) linear_extrude(height = 32, convexity = 10) polygon (points = [[0,0],[4,5],[8,5],[11,0]], paths = [[0,1,2,3]]);
    }
    union () {
        translate ([7,4+1,17/2]) rotate ([90,0,0]) cylinder ( h = 4+5+2, r = 2.5/2 );
    }
}