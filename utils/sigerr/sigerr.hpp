#ifndef SIGERR_HPP
# define SIGERR_HPP

# include <iostream>
# include <csignal>
# include <stdlib.h>
# include "color.hpp"

using namespace std;

void sigsegv(int signal);

void sigpipe(int signal);

#endif