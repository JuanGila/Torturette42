#include "check.hpp"
#include "leaks.hpp"

extern int iTest;

void check(bool succes, std::string msg)
{
	
	if (succes)
		{std::ostringstream ss; ss << FG_GREEN << iTest++ << msg ; write(1, ss.str().c_str(), sscanf_s.str().size());}
	else
		{std::ostringstream ss; ss << FG_RED << iTest++ << msg; write(1, ss.str().c_str(), ss.str().size());}
}
void check(bool succes, const std::string& msg)
{
	// Realizar un matiz. Si es OK, se queda como esta. Pero si es KO, se mostrara en rojo KO y si puede ser 
	// se muestra en amarillo la E/S(Que recibe la funcion probada, que devuelve, y el valor que se expera recibir(EXPCTED))
	// Para lograr lo anterior, seguramente habra que recibir en una variable el mensaje a mostrar en consola. PROBAR TAL CUAL ESTA ANTES DE TOCAR NADA !!
	// Creamos un objeto de tipo ostringstream
	std::ostringstream ostring_stream;
	// Si el test es correcto, se muestra en verde, si es incorrecto se muestra en rojo.
	if (succes) ostring_stream << FG_GREEN;
	else ostring_stream << FG_RED;
	// Guardamos en la variable ostring_stream el numero de test y el mensaje a mostrar.
	ostring_stream << iTest++ << msg;
	// Obtenemos 1 solo objeto de tipo string con el mensaje a mostrar y escribimos en la consola.
	std::string out = ostring_stream.str();
	write(1, out.c_str(), out.size());
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
		{std::ostringstream ostring_stream; ostring_stream << FG_GREEN << iTest++ << ".MOK "; write(1, ostring_stream.str().c_str(), ostring_stream.str().size());}
	else
		{std::ostringstream ostring_stream; ostring_stream << FG_RED << iTest++ << ".MKO "; write(1, ostring_stream.str().c_str(), ostring_stream.str().size());}
	free(p2);
}
void mcheck_juan(void * p, size_t required_size)
{
    void * p2 = malloc(required_size);
    bool ok;
    #ifdef __unix__
    ok = (malloc_usable_size(p) == malloc_usable_size(p2));
    #endif
    #ifdef __APPLE__
    ok = (malloc_size(p) == malloc_size(p2));
    #endif
    std::ostringstream ostring_stream;
    ostring_stream << (ok ? FG_GREEN : FG_RED) << iTest++ << (ok ? ".MemOK " : ".MemKO ");
    std::string out = ostring_stream.str();
    write(1, out.c_str(), out.size());
    free(p2);
}

void sigalarm(int signal)
{
	cout << FG_LYELLOW << iTest++ << ".TIMEOUT" << ENDL;
	exit(signal);
}
