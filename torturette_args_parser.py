#### DEPENDENCIES
### PYTHON
import os
from pathlib import Path
### TORTURETTE TESTER
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
## Comando -> torturette libft info str mem lst | torturette libft info ft_strlen ft_isdigit | torturette libft info ft_strlen test1 test2
# Funcion que obtiene la informacion de un proyecto.
# ATENCION !! Esto se puede usar de forma generica para verificar todo y luego por ultimo comprobamos la acion a realizar para asi ejecutar una funcion que lanza test o que visualiza informacion.
def _get_torturette_project_info(project_name: str, project_targets: list[str]) -> bool:
	# Si no hay targets quiere decir que hay que mostrar toda la info del proyecto recibido en project_name al completo(libft, printf, gnl ...).
	if not project_targets: return _get_common_core_mlst_project_callback(project_name);# _show_libft_tests_info()
	project_targets_set = set(project_targets);
	# Comprobamos si todos los targets recibidos son suites del proyecto recibido.
	if _check_if_project_targets_are_all_suites(project_name, project_targets_set):
		_show_torturette_project_info_by_suites(project_name, project_targets);
	else: return print("Comando mal formado. Si hay al menos 1 suite, todos deben ser suites.");
	# Obtenemos los valores necesarios para realizar las operaciones de busqueda de suites y ejercicios.
	project_tests_exercises_list = _get_project_tests_targets_list(project_name, "exercises");
	project_tests_exercises_set = set(project_tests_exercises_list);
	# project_targets_set <= project_tests_exercises_set → todos los targets son ejercicios(equivalente a issubset()).
	are_project_targets_all_exercises = project_targets_set <= project_tests_exercises_set;
	# Si todos los targets recibidos son ejercicios, realizamos la accion indicada para todos los ejercicios indicados.
	if are_project_targets_all_exercises: _show_torturette_project_info_by_exercises(project_name, project_targets);
	# Comprobamos que el primer elemento de project_targets sea un ejercicio y que el resto de elementos sean tests del ejercicio indicado.
	elif project_targets[0] in project_tests_exercises_set:pass
		#TODO -> FALTA OBTENER LOS TESTS DEL EJERCICIO INDICADO project_targets[0] Y COMPROBAR QUE EL RESTO DE ELEMENTOS DE project_targets ESTEN EN ESA LISTA DE TESTS.
		# Comprobamos que el comando sea -> torturette libft info ft_strlen test1 test2.
	#TODO -> ¿?.
##
def _check_if_project_targets_are_all_suites(project_name: str, project_targets_set: set) -> bool:
	# Obtenemos los valores necesarios para realizar las operaciones de busqueda de suites y ejercicios.
	project_tests_suite_list = _get_project_tests_targets_list(project_name, "suite");
	project_tests_suite_set = set(project_tests_suite_list);
	# project_targets_set <= project_tests_suite_set → todos los targets son suites(equivalente a issubset()).
	are_project_targets_all_suites = project_targets_set <= project_tests_suite_set;
	# project_targets_set & project_tests_suite_set → intersección; si no está vacía, hay al menos una suite.
	have_project_targets_any_suites = bool(project_targets_set & project_tests_suite_set);
	# Si todos los targets recibidos son suites, realizamos la accion indicada para todas las suites indicadas.
	if are_project_targets_all_suites: return True;
	# Si hay al menos 1 suite el comando esta mal formado, ya que si hay al menos 1 suite, todos los targets deben ser suites.
	if have_project_targets_any_suites: return False;
##
def _check_if_project_targets_are_all_exercises(): pass


# Funcion que recibe el nombre de un ejercicio(o suite(revisar esto)) y devuelve la lista de tests que contiene dicho ejercicio(lee el fichero json).
def _get_project_tests_list_of_exercise(exercise_name: str) -> list[str]:pass