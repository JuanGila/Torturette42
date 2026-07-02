#### 4.1.- DEPENDENCIES
### PYTHON
from pathlib import Path
from functools import cache
### TORTURETTE
#¿?
#### 4.2.- FUNCTIONS
### PROJECT-ROOT
## Carpeta root -> /Torturette
# Funcion que encuentra la raiz del proyecto en base a un path recibido(normalmente Path(__file__)).
def _find_project_root(start: Path) -> Path:
    current = start.resolve();
    while current != current.parent:
        if (current / ".git").exists(): return current;
        current = current.parent;
    raise RuntimeError("No se encontró la raíz del proyecto");
#### 4.3.- CONSTANTS
### LIBFT SUITE PATHS
## Carpeta -> /Torturette
# Constante que contiene la ruta de la raiz del proyecto.
_TORTURETTE_PROJECT_ROOT_DIR_PATH: Path = _find_project_root(Path(__file__));
# Constante que contiene la ruta de la carpeta que contiene los tests.
_TORTURETTE_PROJECT_TESTS_DIR_PATH: Path = _TORTURETTE_PROJECT_ROOT_DIR_PATH / "tests";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Libft/*
_TORTURETTE_PROJECT_LIBFT_TESTS_DIR_PATH: Path = _TORTURETTE_PROJECT_TESTS_DIR_PATH / "Libft";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Libft/is/*.c o /Libft/is/*.json
_TORTURETTE_PROJECT_LIBFT_IS_TEST_SUITE_DIR_PATH: Path = _TORTURETTE_PROJECT_LIBFT_TESTS_DIR_PATH / "is";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Libft/fd/*.c o /Libft/fd/*.json
_TORTURETTE_PROJECT_LIBFT_FD_TEST_SUITE_DIR_PATH: Path = _TORTURETTE_PROJECT_LIBFT_TESTS_DIR_PATH / "fd";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Libft/str/*.c o /Libft/str/*.json
_TORTURETTE_PROJECT_LIBFT_STR_TEST_SUITE_DIR_PATH: Path = _TORTURETTE_PROJECT_LIBFT_TESTS_DIR_PATH / "str";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Libft/mem/*.c o /Libft/mem/*.json
_TORTURETTE_PROJECT_LIBFT_MEM_TEST_SUITE_DIR_PATH: Path = _TORTURETTE_PROJECT_LIBFT_TESTS_DIR_PATH / "mem";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Libft/lst/*.c o /Libft/lst/*.json
_TORTURETTE_PROJECT_LIBFT_LST_TEST_SUITE_DIR_PATH: Path = _TORTURETTE_PROJECT_LIBFT_TESTS_DIR_PATH / "lst";
# Variable que contiene las rutas de cada una de las suites del proyecto.
_TORTURETTE_PROJECT_LIBFT_ALL_TESTS_SUITE_DIR_PATHS_DICT = {
	"is": _TORTURETTE_PROJECT_LIBFT_IS_TEST_SUITE_DIR_PATH,
	"str": _TORTURETTE_PROJECT_LIBFT_STR_TEST_SUITE_DIR_PATH,
	"mem": _TORTURETTE_PROJECT_LIBFT_MEM_TEST_SUITE_DIR_PATH,
	"fd": _TORTURETTE_PROJECT_LIBFT_FD_TEST_SUITE_DIR_PATH,
	"lst": _TORTURETTE_PROJECT_LIBFT_LST_TEST_SUITE_DIR_PATH
};
@cache
def _get_libft_all_tests_suite_dir_paths() -> dict[str, Path]:
    return {
        p.name: p
        for p in _TORTURETTE_PROJECT_LIBFT_TESTS_DIR_PATH.iterdir()
        if p.is_dir()
    };
# Funcion que devuelve la ruta de la suite indicada para libft. Se usara para obtener el Path de una suite para extraer de ahi los valores necesarios como los .json
# Es posible que en el futuro haga falta que se devuelva una ruta de paths ya que se podrian recibir varias test-suites.
def _get_libft_all_tests_suite_dir_path(project_suite_name: str) -> Path:
	return  _get_libft_all_tests_suite_dir_paths().get(project_suite_name);
# Iteramos por la ruta /Libft/*/* para extraer de sus carpetas los nombres de los ejercicios ya que se llaman igual.
# Lista que contiene el total de todos los ejercicios a testear.
@cache
def _get_libft_all_tests_suite_exercises_list(
	test_suites_paths: list[Path] = _TORTURETTE_PROJECT_LIBFT_ALL_TESTS_SUITE_DIR_PATHS_DICT.values()
) -> list[str]: return sorted(path.name for test_suite_path in test_suites_paths for path in test_suite_path.iterdir() if path.is_dir());
# Esta funcion puede ser global ya que puede recibir cualquier *_DIR_PATHS_DICT.values() e iterar por los valores(list[Path]).
@cache
def _get_all_tests_suite_exercises_list_by_path(test_suites_paths: list[Path]) -> list[str]:
	return sorted(p.name for path in test_suites_paths for p in path.iterdir() if p.is_dir());


### TODOO OK, NO TOCAR
## FULL SUITE FUNCTIONS
def _get_project_tests_suite_list(project_name: str) -> list[str]:
	# project_name.capitalize() ya que el comando es torturette libft info y la carpeta se llama Torturette/Libft/*
	project_path = _TORTURETTE_PROJECT_TESTS_DIR_PATH / project_name.capitalize();
	# Si la ruta no existe es porque alguien ha modificado la estructura del proyecto.
	if not project_path.is_dir():
		print(f"Error al obtener la lista de suites del proyecto -> {project_name}. Se ha modificado la estructura del proyecto, reinstalar.");
	return [test_suite_path.name for test_suite_path in project_path.iterdir() if test_suite_path.is_dir()];
## FULL EXERCISES FUNCTIONS
def _get_project_tests_exercises_list(project_name: str) -> list[str]:
	# project_name.capitalize() ya que el comando es torturette libft info y la carpeta se llama Torturette/Libft/*
	project_path = _TORTURETTE_PROJECT_TESTS_DIR_PATH / project_name.capitalize();
	# Si la ruta no existe es porque alguien ha modificado la estructura del proyecto.
	if not project_path.is_dir():
		print(f"Error al obtener la lista de suites del proyecto -> {project_name}. Se ha modificado la estructura del proyecto, reinstalar.");
	# Iteramos por las carpetas de la ruta project_path para obtener de cada uno de los directorios los nombres de sus direcotios que son los ejercicios.
	return [
		exercise_path.name
		for test_suite_path in project_path.iterdir()
		for exercise_path in test_suite_path.iterdir()
		if exercise_path.is_dir()
	];
# Funcion que sirve como optimizacion de las anteriores funciones. No usar hasta nueva orden.
def _get_project_tests_targets_list(project_name: str, project_target__type: str = "exercises") -> list[str]:
	# project_name.capitalize() ya que el comando es torturette libft info y la carpeta se llama Torturette/Libft/*
	project_path = _TORTURETTE_PROJECT_TESTS_DIR_PATH / project_name.capitalize();
	# Si la ruta no existe es porque alguien ha modificado la estructura del proyecto.
	if not project_path.is_dir():
		print(f"Error al obtener la lista de suites del proyecto -> {project_name}. Se ha modificado la estructura del proyecto, reinstalar.");
	if project_target__type == "suite": return [test_suite_path.name for test_suite_path in project_path.iterdir() if test_suite_path.is_dir()];
	else: return [
		exercise_path.name
		for test_suite_path in project_path.iterdir()
		for exercise_path in test_suite_path.iterdir()
		if exercise_path.is_dir()
	];