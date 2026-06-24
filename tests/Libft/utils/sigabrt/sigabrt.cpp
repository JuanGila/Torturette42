#include "sigabrt.hpp"
#include "color.hpp"

extern int iTest;

void sigabrt(int signal)
{
	cout << FG_LYELLOW << iTest++ << ".SIGABRT" << ENDL;
	exit(signal);
}
