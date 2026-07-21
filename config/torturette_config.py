
### TORTURETTE
from pathlib import Path
from typing import Callable
#### 4.- CONSTANTS
### 3.1.- ARGUMENT PARSER
_ARGUMENT_PARSER_DEFAULT_ACTIONS_DICT = {
    "info": _get_torturette_project_info,
    "test": _run_torturette_project_tests,
    #"help": _show_torturette_command_help,# dejar esto para el argument parser con --help, es automatico.
    "all": _run_all_torturette_argument_parser_defaults
};
def _get_argument_parser_default_action_callback(action_type: str) -> Callable:
    return _ARGUMENT_PARSER_DEFAULT_ACTIONS_DICT[action_type];
### 3.2.- COMMON CORE
## MILESTONES VALUES
# SIN-USO.Constante que contiene el total de milestones con sus proyectos correspondientes y las funciones que corresponden a cada uno.
_COMMON_CORE_MLST_PROJECTS_DICT = {
    0: {"libft": _show_libft_tests_info},
    1: {
        "printf": _show_printf_tests_info,
        "gnl": _show_gnl_tests_info,
        "push_swap": _show_push_swap_tests_info
    },
    2: {
        "pymod0": _show_pymod0_tests_info, "pymod1": _show_pymod1_tests_info,
        "pymod2": _show_pymod2_tests_info, "pymod3": _show_pymod3_tests_info,
		"pymod4": _show_pymod4_tests_info, "pymod5": _show_pymod5_tests_info,
		"pymod6": _show_pymod6_tests_info, "pymod7": _show_pymod7_tests_info,
		"pymod8": _show_pymod8_tests_info, "pymod9": _show_pymod9_tests_info,
		"pymod10": _show_pymod10_tests_info, "pymod11": _show_pymod11_tests_info,
        "born2beroot": _show_born2beroot_tests_info,
        "a_maze_ing": _show_a_maze_ing_tests_info,
    },
    3: {
        "fly-in": _show_fly_in_tests_info,
        "call_me_maybe": _show_call_me_maybe_tests_info,
        "codexion": _show_codexion_tests_info
	},
	4: {
        "pac-man": _show_pac_man_tests_info,
        "net-practice": _show_net_practice_tests_info,
        "rag": _show_rag_tests_info
	},
	5: {
        "agent-smith": _show_agent_smith_tests_info,
        "answer-protocol": _show_answer_protocol_tests_info,
        "inception": _show_inception_tests_info
    },
	6: {"transcendence": _show_transcendence_tests_info},
}
# SIN-USO.Funcion que devuelve la funcion/callback correspondiente a un proyecto en un milestone.
def _get_common_core_mlst_project_callback(project_name: str) -> Callable | None:
    # Ejemplo: Si project_name es libft y milestone es 0, se devuelve _show_libft_tests_info
    for milestone in _COMMON_CORE_MLST_PROJECTS_DICT.values():
        if project_name in milestone: return milestone[project_name];
	# No se ha encontrado el proyecto indicado. Esto nunca se ejecuta ya que el argumento del proyecto es obligatorio(required=True).
    return None;
# Funcion que devuelve una tupla con el total de proyectos de todos los milestones, osea todos los proyectos del common core.
@cache
def _get_common_core_mlst_projects_tuple() -> tuple[str]:
    # return tuple([project_name for milestone in _COMMON_CORE_MLST_PROJECTS_DICT.values() for project_name in milestone.keys()]); REVISAR ESTO.
	return list(
		project
		for milestone in _COMMON_CORE_MLST_PROJECTS_DICT.values()
		for project in milestone
	);
## HASTA AQUI TODOO OK, NO TOCAR.



### TEST-SUITE DISPATCHER
_COMMON_CORE_TEST_SUITES_LIST = [
	_LIBFT_ALL_TESTS_SUITE_DICT.keys(),
	_PRINTF_TESTS_SUITE_DICT.keys(),
	_GNL_TESTS_SUITE_DICT.keys()
];
def _get_common_core_test_suites_list() -> list[list[str]]: return _COMMON_CORE_TEST_SUITES_LIST;
def _common_core_test_suite_dispatcher(args: list[str] | None = None):
	if args[0] in _get_libft_test_suite_dict_keys(): return _LIBFT_ALL_TESTS_SUITE_DICT[args[0]](args);
	elif args[0] in _get_printf_test_suite_dict_keys(): return _PRINTF_TESTS_SUITE_DICT[args[0]](args);
	elif args[0] in _get_gnl_test_suite_dict_keys(): return _GNL_TESTS_SUITE_DICT[args[0]](args);


#### RUNNERS-TESTERS
_COMMON_CORE_PROJECTS_DICT_ORACULO = {
	"libft": LibftRunner,
    "printf": PrintfRunner,
    "gnl": GnlRunner,
    "push_swap": PushSwapRunner,
};
def _get_torturette_projects_dict_keys_list() -> list[str]: return list(_TORTURETTE_PROJECTS_DICT.keys());