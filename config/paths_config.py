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
    }
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
# mantener tal cual esta hasta nueva revision ya que hay un problema, habria demasiadas constantes con valores dispersos, convendria hacer una variable global con todos los datos de cada proyecto
@cache
def _get_all_tests_suite_exercises_list_by_path(
	test_suites_paths: list[Path] = _TORTURETTE_PROJECT_LIBFT_ALL_TESTS_SUITE_DIR_PATHS_DICT.values()
) -> list[str]: return sorted(p.name for path in test_suites_paths for p in path.iterdir() if p.is_dir());


### PRINTF SUITE PATHS
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Printf
_TORTURETTE_PROJECT_PRINTF_TESTS_DIR_PATH: Path = _TORTURETTE_PROJECT_TESTS_DIR_PATH / "Printf";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Printf/c_flag
_TORTURETTE_PROJECT_PRINTF_CFLAG_TESTS_SUITE_DIR_PATH: Path = _TORTURETTE_PROJECT_PRINTF_TESTS_DIR_PATH / "c_flag";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Printf/s_flag
_TORTURETTE_PROJECT_PRINTF_SFLAG_TESTS_SUITE_DIR_PATH: Path = _TORTURETTE_PROJECT_PRINTF_TESTS_DIR_PATH / "s_flag";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Printf/p_flag
_TORTURETTE_PROJECT_PRINTF_PFLAG_TESTS_SUITE_DIR_PATH: Path = _TORTURETTE_PROJECT_PRINTF_TESTS_DIR_PATH / "p_flag";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Printf/i_flag
_TORTURETTE_PROJECT_PRINTF_IFLAG_TESTS_SUITE_DIR_PATH: Path = _TORTURETTE_PROJECT_PRINTF_TESTS_DIR_PATH / "i_flag";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Printf/d_flag
_TORTURETTE_PROJECT_PRINTF_DFLAG_TESTS_SUITE_DIR_PATH: Path = _TORTURETTE_PROJECT_PRINTF_TESTS_DIR_PATH / "d_flag";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Printf/u_flag
_TORTURETTE_PROJECT_PRINTF_UFLAG_TESTS_SUITE_DIR_PATH: Path = _TORTURETTE_PROJECT_PRINTF_TESTS_DIR_PATH / "u_flag";
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Printf/x_flag
_TORTURETTE_PROJECT_PRINTF_XFLAG_TESTS_SUITE_DIR_PATH: Path = _TORTURETTE_PROJECT_PRINTF_TESTS_DIR_PATH / "x_flag";
_PRINTF_ALL_TESTS_SUITE_DIR_PATHS_DICT = {
	"c_flag": _TORTURETTE_PROJECT_PRINTF_CFLAG_TESTS_SUITE_DIR_PATH,
	"s_flag": _TORTURETTE_PROJECT_PRINTF_SFLAG_TESTS_SUITE_DIR_PATH,
	"p_flag": _TORTURETTE_PROJECT_PRINTF_PFLAG_TESTS_SUITE_DIR_PATH,
	"i_flag": _TORTURETTE_PROJECT_PRINTF_IFLAG_TESTS_SUITE_DIR_PATH,
	"u_flag": _TORTURETTE_PROJECT_PRINTF_UFLAG_TESTS_SUITE_DIR_PATH,
	"x_flag": _TORTURETTE_PROJECT_PRINTF_XFLAG_TESTS_SUITE_DIR_PATH
};
### GNL SUITE PATHS
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Gnl
_TORTURETTE_PROJECT_GNL_TESTS_DIR_PATH: Path = _TORTURETTE_PROJECT_TESTS_DIR_PATH / "Gnl";
_GNL_ALL_TESTS_SUITE_DIR_PATHS_DICT = {};
### PUSH-SWAP SUITE PATHS

### ALL SUITE PATHS
## Variable que contiene un diccionario cuyas claves son los proyectos y los valores
# son diccionarios que contienen las rutas de las suites de cada proyecto.
_ALL_PROJECT_TESTS_SUITE_DIR_PATHS_DICT = {
	"libft": _TORTURETTE_PROJECT_LIBFT_ALL_TESTS_SUITE_DIR_PATHS_DICT,
	"printf": _PRINTF_ALL_TESTS_SUITE_DIR_PATHS_DICT,
	"gnl": _GNL_ALL_TESTS_SUITE_DIR_PATHS_DICT
};
# Funcion que devuelve un diccionario con las rutas de todas las suites del proyecto recibido por parametro.
def _get_project_tests_suite_dir_paths(project_name: str) -> dict[str, Path]:
	return _ALL_PROJECT_TESTS_SUITE_DIR_PATHS_DICT.get(project_name, None);
# Variable que contiene un diccionario cuyas claves son los proyectos y los valores son funciones que obtienen los ejericios del respectivo proyecto.
_ALL_PROJECT_TESTS_EXERCISES_DICT = {
	"libft": _get_libft_all_tests_suite_exercises_list,
	"printf": _get_printf_all_tests_suite_exercises_list,
	"gnl": _get_gnl_all_tests_suite_exercises_list
};
def _get_project_tests_exercises_list(project_name: str) -> list[str]:
	return _ALL_PROJECT_TESTS_EXERCISES_DICT.get(project_name, None);





# POSIBLE OK, NO BORRAR, MEJORAR/ACTUALIZAR
# ¿?
def _get_all_tests_suite_dir_paths(key: str | None = None) -> dict[str, Path] | Path:
	if key is None: return _TORTURETTE_PROJECT_LIBFT_ALL_TESTS_SUITE_DIR_PATHS_DICT.values();
	if key in _TORTURETTE_PROJECT_LIBFT_ALL_TESTS_SUITE_DIR_PATHS_DICT: return _TORTURETTE_PROJECT_LIBFT_ALL_TESTS_SUITE_DIR_PATHS_DICT[key];
	print(f"Key {key} not found in _TORTURETTE_PROJECT_LIBFT_ALL_TESTS_SUITE_DIR_PATHS_DICT");