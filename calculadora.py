def calculadora_simples(numero1, numero2, operador) -> float: # Recebe os números e operador, realiza a operação e retorna o resultado
    if operador == '+':
        resultado = numero1 + numero2
        return resultado
    if operador == '-':
        resultado = numero1 - numero2
        return resultado
    if operador == '*':
        resultado = numero1 * numero2
        return resultado
    if operador == '/':
        resultado = numero1 / numero2
        return resultado
    if operador == '%':
        resultado = numero1 % numero2
        return resultado
    if operador == '**':
        resultado = numero1 ** numero2
        return resultado