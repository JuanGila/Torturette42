#### DEPENDENCIES
### PYTHON
import os
from pathlib import Path
from argparse import ArgumentParser, RawTextHelpFormatter
#### ARGUMENT-PARSER
### Namespace
"""
Namespace(
    project="libft",
    action="test",
    targets=[
        "ft_strlen",
        "test1",
        "test2"
    ]
)
Namespace(
    project="libft",
    action="info",
    targets=["str", "mem"]
)
epilog=
    Uso general: torturette <project> <action> [suite|exercise ...] [test ...]
    
    
    EJEMPLOS;

    LIBFT:
    torturette libft info -> Ejecuta todos los tests de todas las suites.

    torturette libft info is_test -> Ejecuta todos los tests de la suite 'is_test'.

    torturette libft info is_test str_test mem_test -> Ejecuta todas las suites indicadas.

    torturette libft info ft_isdigit -> Ejecuta todos los tests del ejercicio ft_isdigit.

    torturette libft info ft_isdigit ft_isalpha -> Ejecuta todos los tests de los ejercicios ft_isdigit y ft_isalpha.

    torturette libft info ft_isdigit test1 test2 -> Ejecuta únicamente los tests test1 y test2 de ft_isdigit.
    
    PRINTF:
    torturette printf info -> Ejecuta todos los tests del proyecto printf.

    torturette printf info c_flag -> Ejecuta todos los tests del ejercicio c_flag.

    torturette printf info c_flag s_flag -> Ejecuta todos los tests de los ejercicios c_flag y s_flag.

    torturette printf info c_flag test1 test2 -> Ejecuta únicamente los tests test1 y test2 del ejercicio c_flag.
    
    GNL:
    torturette gnl info -> Ejecuta todos los tests del proyecto gnl.

    torturette gnl info c_flag -> Ejecuta todos los tests del ejercicio c_flag.

    torturette gnl info c_flag s_flag -> Ejecuta todos los tests de los ejercicios c_flag y s_flag.

    torturette gnl info c_flag test1 test2 -> Ejecuta únicamente los tests test1 y test2 del ejercicio c_flag."""
def create_argument_parser():
    torturette_argument_parser = ArgumentParser(
        prog="torturette",
        description="42 Common Core Test Runner",
        formatter_class=RawTextHelpFormatter
    );
    ## Comando -> torturette libft o torturette printf
    torturette_argument_parser.add_argument(
        "project",
        choices=_get_common_core_mlst_projects_tuple(),
        metavar="PROJECT",
        help="Proyecto a utilizar."
    );
    ## Comando -> torturette libft info o torturette libft test
    # Argumento que indica la accion a realizar, ya sea info o test.
    torturette_argument_parser.add_argument(
        "action",
        choices=["info", "test"],
        metavar="ACTION",
        help="Acción a realizar."
    );
    ## Comando -> hades libft info str mem o hades libf info ft_strlen ft_isdigit o hades libft info ft_strlen test1 test2
    # Argumento que indica los targets/objetivos de la accion.
    torturette_argument_parser.add_argument(
        "targets",
        nargs="*",
        metavar="TARGET",
        help="Suites, ejercicios o tests."
    );
    # Devolvemos el parser creado.
    return torturette_argument_parser;

""" PLANTILLA KITTY PARA VISUALIZACION DE HELP -> torturette libft help
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 TORTURETTE · LIBFT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📘 USO

  torturette libft <action> [targets...]

⚙️  ACCIONES

  info      Muestra información de las suites.
  test      Ejecuta los tests.
  help      Muestra esta ayuda.

🎯 TARGETS

  suite       Ejecuta una suite completa.
  ejercicio   Ejecuta todos los tests de una función/ejercicio.
  test        Ejecuta únicamente un test.

🌳 JERARQUÍA

  Proyecto
  ├── Suite
  │   ├── ft_strlen
  │   │   ├── basic
  │   │   └── malloc_fail
  │   └── ft_memcpy
  └── ...

💡 EJEMPLOS

  torturette libft test
  torturette libft test str
  torturette libft test ft_strlen
  torturette libft test ft_strlen basic malloc_fail
"""