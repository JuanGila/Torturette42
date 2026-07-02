#### DEPENDENCIES
### PYTHON
import os
from pathlib import Path
from argparse import ArgumentParser, RawTextHelpFormatter
### TORTURETTE TESTER
##
#

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
    targets=["ft_strlen", "test1"]
)
"""
torturette_argument_parser = ArgumentParser(
    prog="torturette",
    description="Torturette Test Runner",
    formatter_class=RawTextHelpFormatter
);
## Comando -> torturette libft o torturette printf
torturette_argument_parser.add_argument(
    "project",
    choices=_COMMON_CORE_MLST_PROJECTS_DICT_TUPLE,
    metavar="PROJECT",
    help="Proyecto a utilizar."
	epilog="""
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
argument_parser_args = torturette_argument_parser.parse_args();
#### Funciones
### AERGUMENT-PARSER
## Comando -> torturette libft info o torturette libft test
# Funcion principal que verifica el argument_parser.
def _check_argument_parser_args(argument_parser_args: list[str]) -> bool:
	if _get_argument_parser_default_action_callback(argument_parser_args.action) is None: return False;
	else: return _get_argument_parser_default_action_callback(argument_parser_args.action)(
		argument_parser_args.project, argument_parser_args.targets
	);
### PROJECTS-HELP
## Comando -> torturette libft help o torturette printf help
# Funcion que muestra la ayuda del comando torturette y el proyecto a utilizar.
def _show_torturette_command_help(project_name: str, project_targets: list[str] | None = None) -> bool:pass
### PROJECTS-INFO
## Comando -> torturette libft info o torturette libft test
# Funcion que obtiene la informacion de un proyecto.
# Posibles targets -> torturette libft info str mem o torturette libft info ft_strlen ft_isdigit o torturette libft info ft_strlen test1 test2
def _get_torturette_project_info(project_name: str, project_targets: list[str]) -> bool:
	# Si no hay targets quiere decir que hay que mostrar toda la info del proyecto recibido en project_name al completo(libft, printf, gnl ...).
	if not argument_parser_args.targets: return _get_common_core_mlst_project_callback(project_name);# __show_libft_tests_info()
	# En base al proyecto recibido, comprobamos que project_targets sean todos suites.
	are_project_targets_all_suites = all(
		_is_argument_parser_target_a_suite(project_name, project_target) for project_target in project_targets
	);
	are_project_targets_any_suites = any(
		_is_argument_parser_target_a_suite(project_name, project_target) for project_target in project_targets
	);
	if are_project_targets_all_suites:pass#TODO -> ¿?
	elif are_project_targets_any_suites: print("Comando mal formado. Si hay al menos 1 suite, todos deben ser suites.");
	# En base al proyecto recibido, comprobamos que project_targets sean todos ejercicios.
	are_project_targets_all_exercises = all(
		_is_argument_parser_target_an_exercise(project_name, project_target) for project_target in project_targets
	);
	if are_project_targets_all_exercises:pass#TODO -> ¿?
	elif any(_is_argument_parser_target_an_exercise(project_name, project_target) for project_target in project_targets):pass
		#TODO -> Comprobamos que el comando sea -> torturette libft info ft_strlen test1 test2.
## FULL SUITES
# Funcion que verifica si el target recibido es una suite(str) del proyecto recibido(libft).
def _is_argument_parser_target_a_suite(project_name: str, project_target: str) -> bool:
	project_tests_suite_list = _get_project_tests_suite_list(project_name);
	# project_tests_suite_list = _get_project_tests_targets_list(project_name, "suite");
	return True if project_target in project_tests_suite_list else False;
## FULL EXERCISES
# Funcion que verifica si tel target recibido es un ejercicio(ft_strlen) del proyecto recibido(libft).
def _is_argument_parser_target_an_exercise(project_name: str, project_target: str) -> bool:
	project_tests_exercises_list = _get_project_tests_exercises_list(project_name);
	# project_tests_suite_list = _get_project_tests_targets_list(project_name, "exercises");
	return True if project_target in project_tests_exercises_list else False;
### PROJECT-TESTS
#
def _run_torturette_project_tests(project_name: str, project_test_targets: list[str]) -> bool:pass