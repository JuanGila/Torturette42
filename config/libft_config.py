#### DEPENDENCIES
### SYSTEM
import os
from pathlib import Path
from functools import cache
#### SUITE FUNCTIONS
##
# Funcion que recibe un proyecto
def _get_project_test_suites_list(project_name: str):pass
##
# Funcion que recibe la ruta por la que iterar para extraer de sus carpetas los nombres de los ejercicios ya que se llaman igual.
@cache
def _get_libft_test_suite_exercises_list(test_suite_path: Path):
    return sorted(p.name for p in test_suite_path.iterdir() if p.is_dir());
##
# Funcion que obtiene las test suites correspondientes al proyecto libft
@cache
def _get_libft_test_suites_list(): return sorted(
	p.name
	for p in _TORTURETTE_PROJECT_LIBFT_TESTS_DIR_PATH.iterdir()
	if p.is_dir()
);