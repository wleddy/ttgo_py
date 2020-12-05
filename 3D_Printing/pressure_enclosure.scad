/*
    openSCAD document
    file name: pressure_enclosure.scad
    created by: William Leddy
*/

// ***************** Parameters ************************
////////////////////////////////////////////////////////
$fn=40;

use </Users/bleddy/Dropbox/3D Printing/SCAD/libraries/enclosure.scad>;

body_size = [30,30,20]; // this is the total Interior space. aprox. (4" X 2" X 1")
lid_height = 4; // Subtracted from body interior height

wall = 2; //2 or 1.6 are good
corner_rad = 0; // 2 is good. Should be <= wall thickness
drill_dia = 3; // fits a #5 FH Screw. 0 to eliminate screw holes and bosses
skirt_depth = 2; // 0 to eliminate skirt otherwise >= 2 is good.
add_lid_nubs=0; // add little nubbs to hold the lid on better
clearance = .1; // used when rendering skirt
render_base = 0; // [1]|0 to render base or not.
render_lid =1; // [1]|0 to render lid or not.


// ***************** Models ****************************
////////////////////////////////////////////////////////

difference(){
    union(){
        enclosure(body_size=body_size,lid_height=lid_height,wall=wall,corner_rad=corner_rad,skirt_depth=skirt_depth,render_base=render_base,render_lid=render_lid,drill_dia=drill_dia,add_lid_nubs=add_lid_nubs); // dimensions are forinterior size

        // translate([0, 22, 0]){
  //       centered_cube(size=[body_size[0]+wall*2, 10, 16]);
  //       translate([0, 0, 5+5])
  //       rotate([90, 0, 0])
  //       cylinder(d=10, h=10, center=true);
  //       }
  //   }
  //   translate([0, 22, 0])
  //   union(){
  //       translate([0, 0, 5+5])
  //       rotate([90, 0, 0]){
  //       translate([0, 0, -5])
  //       cylinder(d1=6.5,d2=5, h=10.1, center=true);
  //       translate([0, 0, 5])
  //       cylinder(d2=6.5,d1=5, h=10.1, center=true);
  //       }
    }
}

// rounded_cube(size=[20,20,20],wall=2,corner_rad=2,
//             flat_top=0,flat_bottom=0,open_bottom=0);

// **************** Modules ****************************
////////////////////////////////////////////////////////



// **************** Helpful Modules ********************
////////////////////////////////////////////////////////

module centered_cube(size=[20,20,20]){
    translate([-(size[0]/2),-(size[1]/2),0]) cube(size);
}

module rounded_cube(size=[20,20,20],wall=0,corner_rad=2,
            flat_top=0,flat_bottom=0,open_bottom=0)
{
    /* 
    make a cube with the corners and top and bottom rounded.
    Top and/or bottom may be made flat.
    If wall > 0, top is flat and an open top box is made
    */
    difference(){
        // add wall to all sides of box
    echo("size:",size,"size[0]",size[0]);
        box(size=[size[0] + wall * 2, size[1] + wall * 2, size[2] + wall * 2]);
        // translate([0, 0, -.01+wall-(wall*open_bottom)])
        // !box(size=[size[0], size[1], size[2] + 100]);
        if(wall > 0){
            echo("hollow box",wall);

            // hollow out the box
            translate([0, 0, -.01+wall-(wall*open_bottom)])
            box(size=[size[0], size[1], size[2] + 100]);
        }
    }
    
    module box(size=size,wall=wall,corner_rad=corner_rad,flat_top=flat_top,flat_bottom=flat_bottom){
        // make the outer box or the cut-out box
        hull(){
            onCorners(size[0]-corner_rad*2,size[1]-corner_rad*2)
            cornerPost(size=size,corner_rad=corner_rad,wall=wall,flat_top=flat_top,flat_bottom=flat_bottom,open_bottom=open_bottom);
        }
    }
    
    module cornerPost(size=size,wall=wall,corner_rad=corner_rad,flat_top=flat_top,flat_bottom=flat_bottom,open_bottom=open_bottom){
        // make the posts for the corner
        union(){
            if(flat_bottom == 0 && open_bottom == 0){ 
                // the rounded bottom
                translate([0, 0, corner_rad])
                difference(){
                    color("green")
                    sphere(r=corner_rad); 
                    centered_cube([corner_rad*2,corner_rad*2,corner_rad]);
                }
            }
            
            // make the post part
            if((flat_bottom == 1 || open_bottom == 1) && (flat_top == 1 || wall > 0) ){
                // top and bottom are flat
                cylinder(r=corner_rad, h=size[2] - wall - (wall * open_bottom), center=false);
            } else if(flat_bottom == 0  && flat_top == 0 && wall <= 0 && open_bottom == 0){
                // full round
                translate([0, 0, corner_rad]) 
                cylinder(r=corner_rad, h=size[2]-corner_rad * 2,center=false);
            } else if(flat_bottom == 1 || open_bottom==1){
                // flat bottom, rounded top
                cylinder(r=corner_rad, h=size[2] + wall - wall * open_bottom -corner_rad ,center=false);
            }else {
                // flat top, rounded bottom
                translate([0, 0, corner_rad]) 
                cylinder(r=corner_rad, h=size[2]-wall-corner_rad ,center=false);
            }
                
            if(flat_top == 0 && wall <= 0){
                //round the top
                translate([0, 0, size[2] - corner_rad])
                difference(){
                 color("red")
                 sphere(r=corner_rad);
                 translate([0, 0, -corner_rad]) 
                     centered_cube([corner_rad*2,corner_rad*2,corner_rad]);
                 }
            }
        }
    }
} // end rounded_cube

module onCorners(rect_x,rect_y,adjust_z=0,cornerInset=0){
    // place the single child on each corner
    for(a = [1,-1]){
        for(b = [-1,1]) {
            translate([((rect_x/2)*a) - (cornerInset * a),((rect_y/2)*b) - (cornerInset * b),adjust_z])
            children(0);
        }
    }
}

module mouseEars(rect_x,rect_y,size=5){
    onCorners(rect_x,rect_y) cylinder(r=size/2,h=.4);
}

module flatheadScrew(screwHoleDia=4,screwHoleDepth=10,screwHeadInset=1){
    screwHeadDia = screwHoleDia * 2.1; // yealds the standard ratio
    screwHeadHeight = screwHeadDia / 2; // heith of coiunter sink cone
    
    union(){
      translate([0, 0, -screwHeadInset+.01]) 
        cylinder(d=screwHeadDia, h=screwHeadInset, center=false);
        // countersink
        cylinder(d1=screwHeadDia,d2=0,h=screwHeadHeight, center=false);
        // shaft
        cylinder(d=screwHoleDia, h=screwHoleDepth, center=false);
    }
    
}


module torus(dia=20, rad=2, centered=false){
    module make_torus(){
        rotate_extrude() translate([dia/2-rad/2 , 0, 0]) circle(d=rad);
    }
     if (centered == false){
         translate([0, 0, rad/2]) make_torus();
     } else { 
         make_torus();
     }
}


module pill(dia=20, rad=2, h=2, centered=false){
    fill_height = h-rad;
    
    module make_pill(){
        cylinder(d=dia-rad, h=rad, center=false);
        translate([0, 0, 0]) torus(dia,rad,centered=false);
        upper_pill(dia,rad,centered);
        
    }
    module upper_pill(dia,rad,centered){
        if(fill_height>rad){
            translate([0, 0, fill_height]) 
            pill(dia,rad,centered);
            translate([0, 0, rad/2]) cylinder(d=dia, h=fill_height, center=false);
        }
    }
     if (centered == false){
         make_pill();
     } else { 
         translate([0, 0, -h/2 ]) 
         make_pill();
     }
}

// convert inches to Millimeters
function ItoM(size) = size * 25.4;

// Get length of one side of right triangle
function triangle_side_len(one_side,another_side) = sqrt(pow(one_side,2)+pow(another_side,2));

// get the angle of the hypotenuse to another side of a right triangle from 
// the length of the hypotenuse and the length of another side
function angle_to_hypotenose(one_side,another_side) = asin(min(one_side,another_side)/max(one_side,another_side));
