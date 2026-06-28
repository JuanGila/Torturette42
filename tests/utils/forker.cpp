//
#include <signal.h>
#include <iostream>
#include <string>
//
pid_t pid = fork();

if (pid == 0)
{
    funcion_a_testear();
    exit(EXIT_SUCCESS);
}

int status;
waitpid(pid, &status, 0);

if (WIFSIGNALED(status))
{
    sigerr(WTERMSIG(status));
}
else if (WIFEXITED(status))
{
    std::cout << iTest++ << ".OK\n";
}