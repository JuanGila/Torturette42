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