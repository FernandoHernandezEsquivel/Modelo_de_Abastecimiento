# Guía de Usuario - Modelo de Abastecimiento

## ¿Para qué sirve este modelo?

El modelo ayuda a responder:
- ¿Cuánto efectivo enviar a cada sucursal?
- ¿Cuándo hacer el envío?
- ¿Qué sucursales tienen mayor riesgo de desabasto?

## Cómo interpretar los outputs

### 1. Plan de Abastecimiento (Excel/CSV)

| Columna | Qué significa | Ejemplo |
|---------|---------------|---------|
| entidad | Estado de la república | Ciudad de México |
| demanda_semanal | Efectivo que se retirará esta semana | $450,000,000 |
| envio_recomendado | Cuánto enviar a esa entidad | $480,000,000 |
| frecuencia_envio | Cada cuántos días enviar | 7 días |

### 2. Alertas

- **Alerta amarilla**: Stock bajo (< 20% del umbral)
- **Alerta roja**: Desabasto inminente (< 48 horas)

### 3. Qué hacer con el plan

1. Revisar las entidades con envío recomendado > $0
2. Coordinar con transportista las rutas
3. Priorizar entidades con alertas
4. Ejecutar envíos antes de las 8 AM