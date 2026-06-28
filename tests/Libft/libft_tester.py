#### DEPENDENCIES
import os
from pathlib import Path
### LIBFT-CONFIG
from config.libft_config import (_get_all_tests_suite_dir_paths,
	_get_libft_is_test_suite_exercises_list, _get_libft_fd_test_suite_exercises_list,
	_get_libft_str_test_suite_exercises_list, _get_libft_mem_test_suite_exercises_list,
	_get_libft_lst_test_suite_exercises_list, _get_libft_all_tests_suite_exercises_list
)
#### LIBFT TEST INFO
###  FULL-SUITES FUNCTIONS
## Funcion que sirve como punto de entrada cuando se ha ejecutado el comando -> torturette libft
# Buscamos que clave del json se corresponde con args[0] COMPROBAR SI AQUI AL ENVIAR [1:] AQUI SE EMPIEZA CON argv[0] O argv[1] en adelante(osea ver si aqui los argumentos son al completo o por partes).
def _show_libft_tests_info(argument_parser_args: list[str] | None = None) -> bool:
	argument_parser_args_has_full_suites_cases_list = False;
	# # argument_parser_args = ["libft"];
	# argument_parser_args = ["libft", "is_test"]; Muestra todos los tests de cada uno de los ejercicios dentro de esa suite.
	if len(argument_parser_args) < 2: return _show_libft_test_suites_info();# HASTA AQUI TODOO OK, NO TOCAR.
	# argument_parser_args = ["libft", "is_test", "str_test"]; Muestra todos los tests de cada uno de los ejercicios dentro de cada suite.
	# argument_parser_args = ["libft", "ft_isdigit", "test1"]; Muestra un test en concreto de un ejercicio de una suite.
	# Si el siguiente argumento a libft es una suit-case comprobamos el resto de suites-cases.
	libft_test_suite_dict_keys_list = _get_libft_test_suite_dict_keys();
	if argument_parser_args[1] in libft_test_suite_dict_keys_list:
		# Si hay 2 suite-cases el resto deben ser tambien suite-cases, sino el comando esta mal formado.
		if argument_parser_args[2] in libft_test_suite_dict_keys_list:
			for test_suit_case in argument_parser_args[3:]:
				if test_suit_case in libft_test_suite_dict_keys_list: continue;
				# print("Error al formar el comando. Use torturette -h para ver la ayuda.");
				if test_suit_case not in libft_test_suite_dict_keys_list: return False;
			#else: argument_parser_args_has_full_suites_cases_list = True;
		# Si hay solo 1 suite-case y no hay mas argumentos, se muestran los tests correspondientes.
		if len(argument_parser_args) == 2:
			#argument_parser_args_has_full_suites_cases_list = True;
			return _LIBFT_ALL_TESTS_SUITE_DICT[argument_parser_args[1]]("REVISAR EL ENVIO DE DATOS");
		else: return False;# Error al formar el comando.
	# Si el siguiente argumento a libft no es una suite-case, y tampoco un ejercicio de una suite en concreto, entonces el comando esta mal formado.
	if argument_parser_args[1] not in _LIBFT_IS_TEST_SUITE_EXERCISES_LIST: return False;
	# Verificamos el ejercicio de una suite en concreto.
### ESPECIFIC TESTS-SUITES
## Comando -> torturette libft o torturette libft [test_suite_list] FUNCION OK -> NO TOCAR
# Funcion que muestra la informacion de todos los test de la suite/apartado -> /Libft/test_suite_list/*/*.json
def _show_libft_test_suites_info(test_suite_list: list[str] = _get_all_tests_suite_dir_paths().keys()) -> bool:
	#for test_suite_name in test_suite_list: _LIBFT_ALL_TESTS_SUITE_DICT[test_suite_name]();
	for test_suite_name in test_suite_list:# test_suite_list = ["is_test", "str-test"];
		tests_suite_dir_path = _get_all_tests_suite_dir_paths(test_suite_name);
		_show_libft_test_suite_info(tests_suite_dir_path);
## Comando -> torturette libft o torturette libft is_test # FUNCION OK -> NO TOCAR
# Funcion que muestra la informacion de todos los test de la suite/apartado -> /Libft/*/*/*.json
def _show_libft_test_suite_info(test_suite_exercises_path: Path) -> bool:
	for dirpath, dirnames, filenames in os.walk(test_suite_exercises_path):
		print(dirpath);
		for dirname in dirnames: _show_libft_test_suite_info(dirname);
		for filename in filenames:
			if filename.endswith(".json"): _show_libft_tests_info(filename);#llamar a una funcion generica que muestre yson sea cual sea(lbft, printf ...)
# Funcion que lee el fichero json correspondiente al recibido por parametro(ft_is*_test.json) y muestra todos sus tests.
def _show_libft_tests_info(test_file_name: str | None = None) -> bool:# Ejecutar funcion del orquestador -> _get_json_file_data();
	# Averiguar de donde cojones saco yo la ruta correspondiente a test_file_name para enviarlo al lector de ficheros json -> _get_json_file_data();
	pass
###  EXERCISES-SUITES FUNCTIONS
### FD
## Comando -> torturette libft ft_putchar_fd o torturette libft ft_putchar_fd ft_putstr_fd
def _show_libft_suite_exercises_tests_info(exercises: list[str] | None = None) -> bool:
	# Iteramos por _LIBFT_FD_TEST_SUITE_EXERCISES_LIST
	# y leemos el atributo "tests" al completo por cada dato en libft_fd_tests.json
	pass
# Comando -> torturette libft ft_putstr_fd test1 test2
def _show_libft_suite_exercise_tests_info(
	exercise_name: str | None = None, exercise_tests: list[int] | None = None
) -> bool:
	# Buscamos en libft_fd_tests.json el ejercicio "exercise_name" y mostramos de su atributo "tests" los test "exercise_tests"
	pass