

void ft_printf_c_flag_tests(void) {
	int printf_res = 0;
	int ft_printf_res = 0;

	ft_printf_res = ft_printf("Test1: %c\n", '!');
	printf_res = printf("Test1: %c\n", '!');
	ft_check_printf_res("Test1(common char)", printf_res, ft_printf_res);
	ft_printf_res = ft_printf("Test1: %c\n", 'a');
	printf_res = printf("Test1: %c\n", 'a');
	ft_check_printf_res("Test1(common char)2", printf_res, ft_printf_res);
	ft_printf_res = ft_printf("Test1: %c\n", ' ');
	printf_res = printf("Test1: %c\n", ' ');
	ft_check_printf_res("Test1(common char)3", printf_res, ft_printf_res);
	ft_printf_res = ft_printf("Test1: %c\n", 'Z');
	printf_res = printf("Test1: %c\n", 'Z');
	ft_check_printf_res("Test1(common char)4", printf_res, ft_printf_res);
	ft_printf_res = ft_printf("Test1: %c\n", '0');
	printf_res = printf("Test1: %c\n", '0');
	ft_check_printf_res("Test1(common char)5", printf_res, ft_printf_res);
	ft_printf_res = ft_printf("Test1: %c\n", '\n');
	printf_res = printf("Test1: %c\n", '\n');
	ft_check_printf_res("Test1(common char)6", printf_res, ft_printf_res);
	ft_printf_res = ft_printf("Test1: %c\n", '\t');
	printf_res = printf("Test1: %c\n", '\t');
	ft_check_printf_res("Test1(common char)7", printf_res, ft_printf_res);
	ft_printf_res = ft_printf("Test1: %c\n", '~');
	printf_res = printf("Test1: %c\n", '~');
	ft_check_printf_res("Test1(common char)8", printf_res, ft_printf_res);
}


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