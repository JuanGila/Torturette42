#### DEPENDENCIES
### PYTHON
import os
from pathlib import Path
### TORTURETTE TESTER
## CONFIG
# Import ¿?
#### TORTURETTE-TESTER FUNCTIONS
### AERGUMENT-PARSER
## Comando -> torturette libft info o torturette libft test
# Funcion principal que verifica el argument_parser.
def _check_argument_parser_args(argument_parser_args: list[str]) -> bool:
	return _get_argument_parser_default_action_callback(argument_parser_args.action)(
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
def _get_torturette_project_info(
	project_name: str = "none_project_name_given",
	project_targets: list[str] = _get_project_tests_targets_list(project_name, "suite")
) -> bool:
	project_targets_set = set(project_targets);
	# Obtenemos los valores necesarios para realizar las operaciones de busqueda de suites y ejercicios.
	project_tests_suite_list = _get_project_tests_targets_list(project_name, "suite");
	project_tests_suite_set = set(project_tests_suite_list);
	# project_targets_set <= project_tests_suite_set → todos los targets son suites(equivalente a issubset()).
	are_project_targets_all_suites = project_targets_set <= project_tests_suite_set;
	# project_targets_set & project_tests_suite_set → intersección; si no está vacía, hay al menos una suite(equivalente a intersection()).
	have_project_targets_any_suites = bool(project_targets_set & project_tests_suite_set);
	# Obtenemos los valores necesarios para realizar las operaciones de busqueda de suites y ejercicios.
	project_tests_exercises_list = _get_project_tests_targets_list(project_name, "exercises");
	project_tests_exercises_set = set(project_tests_exercises_list);
	# project_targets_set <= project_tests_exercises_set → todos los targets son ejercicios(equivalente a issubset()).
	are_project_targets_all_exercises = project_targets_set <= project_tests_exercises_set;
	# Si todos los targets recibidos son suites, realizamos la accion indicada para todas las suites indicadas.
	if are_project_targets_all_suites: return _show_torturette_project_info_by_suites(project_name, project_targets);#esta funcion deberia devolver bool si ha salido bien.
	elif have_project_targets_any_suites: return print("Comando mal formado. Si hay al menos 1 suite, todos deben ser suites.");
	# Si todos los targets recibidos son ejercicios, realizamos la accion indicada para todos los ejercicios indicados.
	elif are_project_targets_all_exercises: return _show_torturette_project_info_by_exercises(project_name, project_targets);#esta funcion deberia devolver bool si ha salido bien.
	# Comprobamos que el primer elemento de project_targets sea un ejercicio y que el resto de elementos sean tests del ejercicio indicado.
	elif project_targets[0] in project_tests_exercises_set:pass
		#TODO -> FALTA OBTENER LOS TESTS DEL EJERCICIO INDICADO project_targets[0] Y COMPROBAR QUE EL RESTO DE ELEMENTOS DE project_targets ESTEN EN ESA LISTA DE TESTS.
		# Comprobamos que el comando sea -> torturette libft info ft_strlen test1 test2.
	else:pass#TODO -> ¿?.
## GENERIC
# Funcion que recibe el nombre de un proyecto y el tipo de target a extraer para devolver la lista de suites o la lista de ejericios del proyecto.
def _get_project_tests_targets_list(
	project_name: str = "none_project_name_given",
	project_target_type: str = "none_project_target_type_given"
) -> list[str]:
	# project_name.capitalize() ya que el comando es torturette libft info y la carpeta se llama Torturette/Libft
	project_path = _TORTURETTE_PROJECT_TESTS_DIR_PATH / project_name.capitalize();
	# Si la ruta no existe es porque alguien ha modificado la estructura del proyecto.
	if not project_path.is_dir():
		print(f"Error al obtener la lista de suites/ejericios del proyecto -> {project_name}. Se ha modificado la estructura del proyecto. Reinstalar.");
	# Si el tipo de target es suite, devolvemos la lista de suites, si es exercises, devolvemos la lista de ejercicios y sino error.
	if project_target_type == "suite": return [test_suite_path.name for test_suite_path in project_path.iterdir() if test_suite_path.is_dir()];
	elif project_target_type == "exercises": return [
		exercise_path.name
		for test_suite_path in project_path.iterdir()
		for exercise_path in test_suite_path.iterdir()
		if exercise_path.is_dir()
	];
	else: raise ValueError(f"Tipo de target no válido -> {project_target_type}. Debe ser 'suite' o 'exercises'.");
## FULL SUITE/EXERCISES FUNCTIONS
# Funcion que muestra la informacion de las suites recibidas en project_targets para el proyecto recibido en project_name.
def _show_torturette_project_info_by_suites(
	project_name: str = "none_project_name",
	project_targets: list[str] = None
) -> bool:
	# project_name.capitalize() ya que el comando es torturette libft info y la carpeta se llama Torturette/Libft/*
	project_path = _TORTURETTE_PROJECT_TESTS_DIR_PATH / project_name.capitalize();
	for project_suite_target in project_targets:
		project_suite_path = project_path / project_suite_target;
		if not project_suite_path.is_dir():
			print(f"Error en la suite -> {project_suite_target} para la ruta -> {project_path}. Se ha modificado la estructura del proyecto. Reinstalar.");
			return False;
		# Mostramos la informacion del .json que hay dentro de la carpeta de cada suite(libft_[project_suite_target]_suite_tests.json). Se lee la suite al completo.
		project_suite_tests_json_file_path = project_suite_path / f"libft_{project_suite_target}_suite_tests.json";
		project_suite_tests_json = json.loads(project_suite_tests_json_file_path.read_text());# refactorizar por -> get_file_data() que a su vez llamara a -> _get_json_data()
		print(json.dumps(project_suite_tests_json, indent = 4));
	else: return True;
#
def _show_torturette_project_info_by_exercises(
	project_name: str = "none_project_name",
	project_targets: list[str] = None
) -> bool:pass
## HASTA AQUI TODOO OK, NO TOCAR.