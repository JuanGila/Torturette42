#### DEPENDENCIES
### SYSTEM
import os
from pathlib import Path
from functools import cache
# Variable que contiene la ruta de la carpeta que contiene los tests de la suite/apartado -> /Libft/*
_TORTURETTE_PROJECT_LIBFT_TESTS_DIR_PATH: Path = _TORTURETTE_PROJECT_TESTS_DIR_PATH / "Libft";
#### SUITE FUNCTIONS
# Funcion que muestra la informacion de todas las suites de libft.
def _show_libft_tests_info():
    libft_test_suites_list = _get_libft_all_tests_suite_dir_paths().keys();
    _show_torturette_project_info_by_suites("libft", libft_test_suites_list)

##
# Funcion que devuelve un diccionario cuyas claves son los nombres de las suites de libft y cuyos valores son las rutas de dichas suites.-
@cache
def _get_libft_all_tests_suite_dir_paths() -> dict[str, Path]:
    return {
        p.name: p
        for p in _TORTURETTE_PROJECT_LIBFT_TESTS_DIR_PATH.iterdir()
        if p.is_dir()
    };
# Funcion que devuelve la ruta de la suite indicada para libft.
# Se usara para obtener el Path de una suite para extraer de ahi los valores necesarios como los .json
def _get_libft_all_tests_suite_dir_path(project_suite_name: str) -> Path:
	return  _get_libft_all_tests_suite_dir_paths().get(project_suite_name);