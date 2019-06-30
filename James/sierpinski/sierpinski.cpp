//################################
//#                              #
//#      Sierpinski.cpp          #
//#                              #
//################################

#include "GL/freeglut.h"
#include "GL/gl.h"

int main(int argc, char **argv)
{

   glutInit(&argc, argv);
   glutInitDisplayMode(GLUT_SINGLE);
   glutInitWindowSize(800, 800);
   glutInitWindowPosition(100, 100);
   glutCreateWindow("OpenGL - Sierpinski");
   glutMainLoop();
   
   return 0;


}

    
