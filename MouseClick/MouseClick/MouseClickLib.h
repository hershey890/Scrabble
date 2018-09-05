#ifndef MOUSECLICKLIB_H
#define MOUSECLICKLIB_H

class MouseClick {
private:
public:
	MouseClick(void);
	int xPos(void);
	int yPos(void);
	//bool isRButtonDown(void);
	//bool isLButtonDown(void);
	bool KeyIsPressed(unsigned char k);
};

#endif