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

   glColor3f(1.0, 1.0, 0.5);
   glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);
  // gl_PointSize = 2.0;
  // for this to work we need an array of points
  // glDrawArrays(GL_POINTS, 0, 3)

   glBegin(GL_LINE_LOOP);
      glVertex3f(-1.0, -1.0, 0.0);
      glVertex3f(0.0, 0.5, 0.0);
      glVertex3f(1.0, -1.0, 0.0);
   glEnd();

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

    
