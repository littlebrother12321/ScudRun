//################################
//#                              #
//#      Sierpinski.cpp          #
//#                              #
//################################

#include "GL/freeglut.h"
#include "GL/gl.h"

void drawDot()
{
   glClearColor(0.4, 0.4, 0.4, 0.4);
   glClear(GL_COLOR_BUFFER_BIT);


   glFlush();

}

int main(int argc, char **argv)
{

   glutInit(&argc, argv);
   glutInitDisplayMode(GLUT_SINGLE);
   glutInitWindowSize(800, 800);
   glutInitWindowPosition(100, 100);
   glutCreateWindow("OpenGL - Sierpinski");

   glutDisplayFunc(drawDot);

   glutMainLoop();

   
   
   return 0;


}

    
