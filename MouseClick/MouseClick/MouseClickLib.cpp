#include "MouseClickLib.h"
#include <windowsx.h>
#include <Windows.h>

/*  Macros: Define the x and y coordinates of the mouse pointer */
//int xPos = GET_X_LPARAM(LPARAM);
// int yPos = GET_Y_LPARAM(LPARAM);

/********************************************************************
* CONSTRUCTOR
* Windows does not allow double clicks by default and
* this allows for it
*********************************************************************/
MouseClick::MouseClick(void) {
	WNDCLASS wc = {};
	wc.style = CS_DBLCLKS;

	/* Set other structure members */
	RegisterClass(&wc);
}

static PyObject MouseClick::*MouseClick_system(PyObject *self, PyObject *args) {
	const char *command;
	int sts;

	if (!PyArg_ParseTuple(args, "s", &command))
		return NULL;
	sts = system(command);
	return Py_BuildValue("i", sts);
}


int MouseClick::xPos(void) {
	/* Gives cursor position relative to screen */
	POINT p;
	if (GetCursorPos(&p)) {
		return p.x;
		//cursor position now in p.x and p.y
	}
	return -1;
	/* maps to window coordinates */
	//if (ScreenToClient(hwnd, &p)) {
	//	return p.x;
		//p.x and p.y are now relative the hwnd's client area
	//}
	/* can also hide and show cursor with showcursor */
	//ShowCursor(FALSE); //hides the cursor
	//ShowCursor(TRUE); //shows it again
	
}

int MouseClick::yPos(void) {
	/* Gives cursor position relative to screen */
	POINT p;
	if (GetCursorPos(&p)) {
		return p.y;
	}
	return -1;
}

//bool MouseClick::isRButtonDown(void) {
//	WPARAM wparam;
//	GetKeyState
//	return (wparam & MK_LBUTTON) ? true : false;
//}
//
//bool MouseClick::isLButtonDown(void) {
//	WPARAM wparam = GET_WPARAM(wparam);
//	return (wparam & MK_RBUTTON) ? true : false;
//}

bool MouseClick::KeyIsPressed(unsigned char k) {
	USHORT status = GetAsyncKeyState(k);
	return (((status * 0x8000) >> 15) == 1) || ((status & 1) == 1);
}