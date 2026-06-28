//
#include <signal.h>
#include <iostream>
#include <string>
#include "sigerr.hpp"
#include "color.hpp"
//
extern int iTest;
// SIGERR (global error)
void sigerr(int signal, std::string& msg)
{
    // Usar este global para todos. Crear una funcion que recoja los errores y cuando detecte cual es cual cree el mensaje correspondiente.
    cout << FG_LYELLOW << iTest++ << msg << ENDL;
    exit(signal);
}
void sigerr(int signal)
{
    static const struct
    {
        int sig;
        const char *msg;
    } errors[] =
    {
        { SIGSEGV, ".SIGSEGV (Segmentation Fault)" },
        { SIGABRT, ".SIGABRT (Abort)" },
        { SIGFPE,  ".SIGFPE (Floating Point Exception)" },
        { SIGILL,  ".SIGILL (Illegal Instruction)" },
        { SIGBUS,  ".SIGBUS (Bus Error)" },
        { SIGPIPE, ".SIGPIPE (Broken Pipe)" },
        { SIGTERM, ".SIGTERM (Terminated)" },
        { SIGINT,  ".SIGINT (Interrupted)" }
    };
    for (size_t i = 0; i < sizeof(errors) / sizeof(errors[0]); ++i)
    {
        if (errors[i].sig == signal)
        {
            std::cout << iTest++ << errors[i].msg << '\n';
            return;
        }
    }
    std::cout << iTest++ << ".UNKNOWN SIGNAL (" << signal << ")\n";
}
// SIGSEGV (segmentation fault)
void sigsegv(int signal)
{
	cout << FG_LYELLOW << iTest++ << ".SIGSEGV" << ENDL;
	exit(signal);
}
// SIGABRT (abort)
void sigabrt(int signal)
{
	cout << FG_LYELLOW << iTest++ << ".SIGABRT" << ENDL;
	exit(signal);
}
// SIGFPE (error de punto flotante)
void sigfpe(int signal)
{
    cout << FG_LYELLOW << iTest++ << ".SIGFPE" << ENDL;
    exit(signal);
}
// SIGILL (instrucción ilegal)
void sigill(int signal)
{
    cout << FG_LYELLOW << iTest++ << ".SIGILL" << ENDL;
    exit(signal);
}
//SIGBUS (error de acceso a memoria alineada o mapeada)
void sigbus(int signal)
{
    cout << FG_LYELLOW << iTest++ << ".SIGBUS" << ENDL;
    exit(signal);
}
// SIGPIPE (escribir en un pipe cerrado)
void sigpipe(int signal)
{
	cout << FG_LYELLOW << iTest++ << ".SIGPIPE" << ENDL;
	exit(signal);
}
// SIGTERM (terminación solicitada)
void sigterm(int signal)
{
    cout << FG_LYELLOW << iTest++ << ".SIGTERM" << ENDL;
    exit(signal);
}
/*
Los 10 más habituales en entrevistas y depuración de C
Si tuviera que elegir los más frecuentes en código real:

Buffer Overflow
Use After Free
Memory Leak
Double Free
NULL Pointer Dereference
Stack Overflow
Heap Corruption
SIGABRT (asserts)
SIGFPE (división por cero)
Deadlocks (si hay multithreading)

Sí. De hecho, si estás usando fork() para ejecutar cada test en un proceso hijo, no necesitas un manejador distinto para cada señal (sigsegv, sigabrt, etc.). Puedes tener una única función que traduzca el número de señal a un mensaje.

La idea es:

El hijo ejecuta la función a testear.
Si el hijo muere por una señal, el padre la detecta con waitpid().
Una función convierte la señal en el texto correspondiente.

*/