#include "MouseClickLib.h"
#include <Windows.h>
#include <iostream>

int main(void) {
	MouseClick mouse;
	while (true) {
		std::cout << "x: " << mouse.xPos() << " y: " << mouse.yPos() << std::endl;
		if (mouse.KeyIsPressed(MK_LBUTTON)) {
			std::cout << "Left button down" << std::endl;
			break;
		}
	}
}