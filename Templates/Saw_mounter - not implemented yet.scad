$fn = 60;
difference () {
    union () {
	cube ( size = [20,25,15]); //Basisblock
	translate ([0,-8,5]) cube ( size = [9,8,9]);
        translate ([0,0,15]) cube ( size = [20,25/4,15*0.5]); //Angle Connector 1
        translate ([0,25-25/4,15]) cube ( size = [20,25/4,15*0.5]); // Angle Connector 2
	translate ([20/2,25/4,15*1.5]) rotate ([90,0,0]) cylinder ( h = 25/4, r = 20/2 ); // Angle 1
	translate ([20/2,25,15*1.5]) rotate ([90,0,0]) cylinder ( h = 25/4, r = 20/2 ); // Angle 2
    }
    union () {
        translate ([20/2,-1,15*1.65]) rotate ([-90,0,0]) cylinder ( h = 25+2, r = 8/2); // Screw Shaft 1
        translate ([9/2,-8-1,5+9/2]) rotate ([-90,0,0]) cylinder ( h = 15, r = 2.5/2); // Screw Shaft 1
	translate ([20/2,25/2+25/4,15*1.65]) rotate ([90,0,0]) cylinder ( h = 25/2, r = 20/2 ); // Angle Space
// 	translate ([-1,20/4,2]) cube ( size = [20+2,20/2,1]);
	translate ([20/2,25/2,-1]) cylinder ( h = 9, r = 10/2); // Press-In Space
	translate ([20/2,25/2,2+1-1]) cylinder ( h = 15, r = 2.5/2); // Press-In Screw
	
	translate ([20/4,25/2,-24]) rotate ([270,0,-90]) { // Belt Corridor
            difference () {
                cylinder ( h = 10, r = 65/2 );
                translate ([0,0,-1]) cylinder ( h = 12, r = 60/2 );
            }
        }
        translate ([-1,25/2,-31]) rotate ([270,0,-90]) cylinder ( h = 20+2, r = 65/2 ); // Tool Handle Nosefitting

    }
}

