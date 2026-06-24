#include "check.hpp"
#include "leaks.hpp"

extern int iTest;

void check(bool succes, std::string msg)
{
	// Realizar un matiz. Si es OK, se queda como esta. Pero si es KO, se mostrara en rojo KO y si puede ser 
	// se muestra en amarillo la E/S(Que recibe la funcion probada, que devuelve, y el valor que se expera recibir(EXPCTED))
	// Para lograr lo anterior, seguramente habra que recibir en una variable el mensaje a mostrar en consola. PROBAR TAL CUAL ESTA ANTES DE TOCAR NADA !!
	if (succes)
		{std::ostringstream ss; ss << FG_GREEN << iTest++ << msg ; write(1, ss.str().c_str(), ss.str().size());}
	else
		{std::ostringstream ss; ss << FG_RED << iTest++ << msg; write(1, ss.str().c_str(), ss.str().size());}
}

void mcheck(void * p, size_t required_size)
{
	void * p2 = malloc(required_size);
	#ifdef __unix__
	if (malloc_usable_size(p) == malloc_usable_size(p2))
	#endif
	#ifdef __APPLE__
	if (malloc_size(p) == malloc_size(p2))
	#endif
		{std::ostringstream ss; ss << FG_GREEN << iTest++ << ".MOK "; write(1, ss.str().c_str(), ss.str().size());}
	else
		{std::ostringstream ss; ss << FG_RED << iTest++ << ".MKO "; write(1, ss.str().c_str(), ss.str().size());}
	free(p2);
}

void sigalarm(int signal)
{
	cout << FG_LYELLOW << iTest++ << ".TIMEOUT" << ENDL;
	exit(signal);
}
