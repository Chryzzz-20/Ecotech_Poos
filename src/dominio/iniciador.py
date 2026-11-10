import requests

from servicios.permisos import exigir_sesion

def obtener_datos():
    respuesta = requests.get(
        "https://mindicador.cl/api/dolar",
        timeout=(3, 5),
    )
    respuesta.raise_for_status()
    return respuesta.json()

import math

def extraer_primero(datos):
    if not isinstance(datos, dict):
        raise ValueError("Respuesta inesperada.")

    serie = datos.get("serie")

    if not isinstance(serie, list) or not serie:
        raise ValueError("No hay valores disponibles.")

    registro = serie[0]
    valor = registro["valor"]

    if (
        type(valor) not in (int, float)
        or not math.isfinite(valor)
        or valor <= 0
    ):
        raise ValueError("Valor del indicador inválido.")

    return registro["fecha"], valor

try:
    datos = obtener_datos()
    fecha, valor = extraer_primero(datos)

    print(f"Dólar observado: {valor:.2f} CLP por USD")
    print(f"Fecha del registro: {fecha}")

except requests.exceptions.RequestException:
    print("No pudimos consultar el servicio. Reintente.")

except (ValueError, KeyError, TypeError):
    print("La respuesta no contiene un indicador válido.")

class Indicador:
    def __init__(self, fecha, valor, verificado_en=None,
                fuente="api_dolar_curso"):
        
        self.fecha = fecha
        self.valor = valor
        self.fuente = fuente
        self.codigo = "dolar"
        self.unidad = "CLP/USD"
        self.verificado_en = verificado_en

def obtener_historial(sesion):
    exigir_sesion(sesion)
    return IndicadorDAO.listar()

historial = obtener_historial(usuario_actual)
for dato in historial:
    print(f"{dato.fecha}: {dato.valor:.2f} {dato.unidad}")