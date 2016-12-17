 
difference () {
    union () {
        linear_extrude(height = 2.5, convexity = 10) import("Junction-Box_1.dxf");
        translate ([0,0,2.5]) linear_extrude(height = 17, convexity = 10) import("Junction-Box_2.dxf");
    }
    union () {
        translate ([8,4,20]) rotate ([0,90,0]) cylinder ( h = 30, r = 8.3/2);
        translate ([146,143,10]) rotate ([90,90,0]) cylinder ( h = 30, r = 8.3/2);
        translate ([141,113,10]) cube ( size = [10,30,20]);
    }
}
