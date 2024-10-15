def calcular_total_factura(cantidad_sin_iva, iva=21):
    
    total_con_iva = cantidad_sin_iva + (cantidad_sin_iva * iva / 100)
    return total_con_iva


total = calcular_total_factura(100) 
print(f"Total con IVA: {total}")

total_personalizado = calcular_total_factura(100, 15)
print(f"Total con IVA personalizado: {total_personalizado}")
