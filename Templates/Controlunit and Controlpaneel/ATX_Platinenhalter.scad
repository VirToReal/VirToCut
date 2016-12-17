/*
difference () {
 union () {
   linear_extrude(height = 1.5, convexity = 10) import("Anordnung V3_Layer1.dxf"); 
   translate ([0,0,1.5]) linear_extrude(height = 16.5, convexity = 10) import("Anordnung V3_Layer12_bind.dxf");
 }
 union () {
   translate ([0,0,2.5+16.5-5]) linear_extrude(height = 6, convexity = 10) import("Anordnung V3_Layer12_bind_holes.dxf"); 
 }
}*/

translate ([0,0,17.5]) linear_extrude(height = 3, convexity = 10) import("Anordnung V3_Layer2.dxf");