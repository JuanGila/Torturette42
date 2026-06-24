
void ft_printf_c_flag_tests(void) {
    int printf_res;
    int ft_printf_res;

    // Puntero a variable local
    TEST("%c", '!');
    TEST("%c", 'a');
    TEST("%c", 'Z');
    TEST("%c", '0');
    TEST("%c", ' ');
    TEST("%c", '\n');
    TEST("%c", '\t');
    TEST("%c", '~');
    // USAR LA MACRO
    ft_printf_res = ft_printf("Test1: %p\n", &x);
    printf_res = printf("Test1: %p\n", &x);
    ft_check_printf_res("Pointer to int", printf_res, ft_printf_res);
}