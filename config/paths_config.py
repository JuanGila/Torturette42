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
    # Lca carpeta raiz sera enconrada cuando sea Torturette/
    current = start.resolve();
    while not ((current / "tests").is_dir() and (current / "testers").is_dir()): current = current.parent;
    if ((current / "tests").is_dir() and (current / "testers").is_dir()): return current;
    else: raise RuntimeError("No se encontró la raíz del proyecto o el mismo esta corrupto(estructura modificada). Reinstalar.");
#### 4.3.- CONSTANTS
### LIBFT SUITE PATHS
## Carpeta -> /Torturette
# Constante que contiene la ruta de la raiz del proyecto.
_TORTURETTE_PROJECT_ROOT_DIR_PATH: Path = _find_project_root(Path(__file__));
# Constante que contiene la ruta de la carpeta que contiene los tests.
_TORTURETTE_PROJECT_TESTS_DIR_PATH: Path = _TORTURETTE_PROJECT_ROOT_DIR_PATH / "tests";


##
# Funcion que recibe la ruta de la suite por la que iterar para extraer de sus carpetas los nombres de los ejercicios ya que se llaman igual.
@cache
def _get_all_tests_suite_exercises_list_by_path(test_suite_path: Path) -> list[str]: return sorted(
	exercise_dir_path.name
	for exercise_dir_path in test_suite_path.iterdir()
	if exercise_dir_path.is_dir()
);