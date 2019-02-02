#include <GL/glew.h>
#ifdef FREEGLUT
#include <GL/freeglut.h>
#else
#include <GL/glut.h>
#endif


int main(int argc, char **argv)
{
	glutInit(&argc, argv);            //Initializes GLUT
	glutInitDisplayMode(GLUT_SINGLE); //Set up Display Buffer
	glutInitWindowSize(500, 500);     //Set window size
	glutInitWindowPosition(100, 100); //Set window location
	glutCreateWindow("OpenGL");       //Create the window
}