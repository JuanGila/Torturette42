#include <stdio.h>
#include <stdlib.h>

void ft_printf_p_flag_tests(void) {
    int printf_res;
    int ft_printf_res;

    int x = 42;
    int y = 84;
    char c = 'A';
    char *str = "Hola";
    int array[5] = {1, 2, 3, 4, 5};
    void *heap = malloc(sizeof(int));

    // Puntero a variable local
    ft_printf_res = ft_printf("Test1: %p\n", &x);
    printf_res = printf("Test1: %p\n", &x);
    ft_check_printf_res("Pointer to int", printf_res, ft_printf_res);

    // Puntero a char
    ft_printf_res = ft_printf("Test2: %p\n", &c);
    printf_res = printf("Test2: %p\n", &c);
    ft_check_printf_res("pointer to char", printf_res, ft_printf_res);

    // Puntero a string
    ft_printf_res = ft_printf("Test3: %p\n", str);
    printf_res = printf("Test3: %p\n", str);
    ft_check_printf_res("pointer to string", printf_res, ft_printf_res);

    // Dirección del array
    ft_printf_res = ft_printf("Test4: %p\n", array);
    printf_res = printf("Test4: %p\n", array);
    ft_check_printf_res("pointer to array", printf_res, ft_printf_res);

    // Dirección de un elemento del array
    ft_printf_res = ft_printf("Test5: %p\n", &array[3]);
    printf_res = printf("Test5: %p\n", &array[3]);
    ft_check_printf_res("pointer to array element", printf_res, ft_printf_res);

    // Puntero obtenido con malloc
    ft_printf_res = ft_printf("Test6: %p\n", heap);
    printf_res = printf("Test6: %p\n", heap);
    ft_check_printf_res("malloc pointer", printf_res, ft_printf_res);

    // Puntero nulo
    ft_printf_res = ft_printf("Test7.1: %p\n", (void *)0);
    printf_res = printf("Test7.1: %p\n", (void *)0);
    ft_check_printf_res("NULL pointer((void *)0)", printf_res, ft_printf_res);
    // Si #define NULL 0, enotnces posible UB(Undefined Behavior/Comportamiento indefinido).
    ft_printf_res = ft_printf("Test7.2: %p\n", NULL);
    printf_res = printf("Test7.2: %p\n", NULL);
    ft_check_printf_res("NULL pointer(NULL)", printf_res, ft_printf_res);

    // Dos punteros en la misma llamada
    ft_printf_res = ft_printf("Test8: %p %p\n", &x, &y);
    printf_res = printf("Test8: %p %p\n", &x, &y);
    ft_check_printf_res("two different pointers", printf_res, ft_printf_res);

    // Mismo puntero repetido
    ft_printf_res = ft_printf("Test9: %p %p %p\n", &x, &x, &x);
    printf_res = printf("Test9: %p %p %p\n", &x, &x, &x);
    ft_check_printf_res("same pointer repeated", printf_res, ft_printf_res);

    // Puntero a puntero
    int *pointer = &y;
    ft_printf_res = ft_printf("Test10: %p\n", &pointer);
    printf_res = printf("Test10: %p\n", &pointer);
    ft_check_printf_res("pointer to pointer", printf_res, ft_printf_res);

    // Puntero Con Limites Positivos
    ft_printf_res = ft_printf("Test11: %p\n", (void *)LONG_MAX);
    printf_res = printf("Test11: %p\n", (void *)LONG_MAX);
    ft_check_printf_res("pointer with positive limits", printf_res, ft_printf_res);

    // Puntero Con Limites Negativos
    ft_printf_res = ft_printf("Test12: %p\n", (void *)LONG_MIN);
    printf_res = printf("Test12: %p\n", (void *)LONG_MIN);
    ft_check_printf_res("pointer with negative limits", printf_res, ft_printf_res);
    // FREE
    free(heap);
}