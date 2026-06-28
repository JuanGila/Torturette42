#!/usr/bin/env bash

# Colores
RESET="\033[0m"
BOLD="\033[1m"

BLUE="\033[38;5;39m"
GREEN="\033[38;5;46m"
RED="\033[38;5;196m"
YELLOW="\033[38;5;220m"

# Datos
DATA=(
    "ft_strncmp|test01|Comparar cadenas iguales|ret == 0|ret != 0|NULL ptr"
    "ft_strncmp|test02|Comparar primer caracter distinto|ret < 0|ret >= 0|NULL ptr"
    "s_flag|test01|Detectar la flag s|flag encontrada|flag ausente|overflow"
)

HEADERS=(
    "🎯 TARGET"
    "🧪 TEST"
    "📚 OBJETIVO"
    "✓ OK"
    "✗ KO"
    "💥 CRASH"
)

# Inicializar anchos con los headers
for i in "${!HEADERS[@]}"; do
    WIDTHS[$i]=${#HEADERS[$i]}
done

# Calcular ancho máximo por columna
for row in "${DATA[@]}"; do
    IFS='|' read -ra cols <<< "$row"

    for i in "${!cols[@]}"; do
        len=${#cols[$i]}
        (( len > WIDTHS[$i] )) && WIDTHS[$i]=$len
    done
done

repeat_char()
{
    local char="$1"
    local count="$2"

    printf "%${count}s" "" | tr ' ' "$char"
}

print_separator()
{
    local left="$1"
    local mid="$2"
    local right="$3"

    printf "%s" "$left"

    for i in "${!WIDTHS[@]}"; do
        printf "%s" "$(repeat_char "─" $((WIDTHS[$i] + 2)))"

        if (( i < ${#WIDTHS[@]} - 1 )); then
            printf "%s" "$mid"
        fi
    done

    printf "%s\n" "$right"
}

print_header()
{
    print_separator "┌" "┬" "┐"

    printf "│"

    for i in "${!HEADERS[@]}"; do
        printf " ${BOLD}${BLUE}%-*s${RESET} │" \
            "${WIDTHS[$i]}" \
            "${HEADERS[$i]}"
    done

    printf "\n"

    print_separator "├" "┼" "┤"
}

print_row()
{
    local row="$1"

    IFS='|' read -ra cols <<< "$row"

    printf "│ %-*s │ %-*s │ %-*s │ ${GREEN}%-*s${RESET} │ ${RED}%-*s${RESET} │ ${YELLOW}%-*s${RESET} │\n" \
        "${WIDTHS[0]}" "${cols[0]}" \
        "${WIDTHS[1]}" "${cols[1]}" \
        "${WIDTHS[2]}" "${cols[2]}" \
        "${WIDTHS[3]}" "${cols[3]}" \
        "${WIDTHS[4]}" "${cols[4]}" \
        "${WIDTHS[5]}" "${cols[5]}"
}

print_footer()
{
    print_separator "└" "┴" "┘"
}

print_header

for row in "${DATA[@]}"; do
    print_row "$row"
done

print_footer


"
┌────────────┬────────┬────────────────────────────────┬──────────┬──────────┬───────────┐
│ TARGET     │ TEST   │ OBJETIVO                       │ OK       │ KO       │ CRASH     │
├────────────┼────────┼────────────────────────────────┼──────────┼──────────┼───────────┤
│ ft_strncmp │ test01 │ Comparar cadenas iguales       │ ret == 0 │ ret != 0 │ NULL ptr  │
│ ft_strncmp │ test02 │ Comparar primer caracter ...   │ ret < 0  │ ret >= 0 │ NULL ptr  │
│ s_flag     │ test01 │ Detectar la flag s             │ flag ... │ flag ... │ overflow  │
└────────────┴────────┴────────────────────────────────┴──────────┴──────────┴───────────┘
"