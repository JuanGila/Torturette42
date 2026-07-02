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

### PRINTF TEST INFO -> argument_parser_args.args
## Comando -> torturette printf
# Funcion que lee la informacion de todos los ficheros json. Las claves json que se leeran seran los valores recibidos en los argumentos.
def _show_printf_tests_info(args: str | None = None) -> bool: pass
## Comando -> torturette printf c_flag o torturette printf c_flag test1
def _show_printf_c_flag_tests_info(args: str | None = None) -> bool: pass
## Comando -> torturette printf s_flag o torturette printf s_flag test1
def _show_printf_s_flag_tests_info(args: str | None = None) -> bool: pass
## Comando -> torturette printf p_flag o torturette printf p_flag test1
def _show_printf_p_flag_tests_info(args: str | None = None) -> bool: pass
## Comando -> torturette printf d_flag o torturette printf d_flag test1
def _show_printf_d_flag_tests_info(args: str | None = None) -> bool: pass
## Comando -> torturette printf i_flag o torturette printf i_flag test1
def _show_printf_i_flag_tests_info(args: str | None = None) -> bool: pass
## Comando -> torturette printf u_flag o torturette printf u_flag test1
def _show_printf_u_flag_tests_info(args: str | None = None) -> bool: pass
## Comando -> torturette printf x_flag o torturette printf x_flag test1
def _show_printf_x_flag_tests_info(args: str | None = None) -> bool: pass
## Comando -> torturette printf X_flag o torturette printf X_flag test1
def _show_printf_X_flag_tests_info(args: str | None = None) -> bool: pass
## Comando -> torturette printf percent_flag o torturette printf percent_flag test1
def _show_printf_percent_flag_tests_info(args: str | None = None) -> bool: pass
_PRINTF_TESTS_SUITE_DICT = {
    "c_flag": _show_printf_c_flag_tests_info,
    "s_flag": _show_printf_s_flag_tests_info,
    "p_flag": _show_printf_p_flag_tests_info,
    "d_flag": _show_printf_d_flag_tests_info,
    "i_flag": _show_printf_i_flag_tests_info,
    "u_flag": _show_printf_u_flag_tests_info,
    "x_flag": _show_printf_x_flag_tests_info,
    "X_flag": _show_printf_X_flag_tests_info,
    "percent_flag": _show_printf_percent_flag_tests_info
};
def _get_printf_test_suite_dict_keys() -> list[str]: return list(_PRINTF_TESTS_SUITE_DICT.keys());