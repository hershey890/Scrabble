#ifndef MOUSECLICKLIB_H
#define MOUSECLICKLIB_H

#include <Python.h>

class MouseClick {
	/* The static was given in the example but may be unecessary seeing as this is C++ not C and private
	 * is already beubg used */
private:
	/*static*/ 
	PyObject *MouseClick_system(PyObject *self, PyObject *args);
public:
	MouseClick(void);
	int xPos(void);
	int yPos(void);
	bool KeyIsPressed(unsigned char k);
};

#endif