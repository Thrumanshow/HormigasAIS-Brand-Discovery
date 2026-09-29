# Data Dictionary — HormigasAIS Brand Discovery

## Identificación

### experiment_id

Identificador del experimento.

Ejemplo:

`EXP001`

### variant

Variante experimental.

Ejemplos:

`A`, `B`, `C`

## Branding

### brand_added_in_edit

Indica si se añadió texto o elemento de marca durante la edición.

### original_brand_visible

Indica si la marca ya estaba presente en el contenido original.

Estas dos variables no deben confundirse.

## Índice emocional

El índice emocional describe características observables o intencionales del contenido.

No representa un perfil psicológico del espectador.

Campos:

- emotion_primary
- emotion_secondary
- valence
- arousal
- tension
- controversy
- hook_type
- target_action
- evidence
- confidence

## Métricas

Las métricas pueden incluir:

- views
- reach
- likes
- comments
- shares
- saves
- profile_visits
- retention

## Datos pendientes

Los valores desconocidos deben permanecer vacíos o `null`.

Nunca inventar métricas, fechas, URLs o duración.

## Regla de codificación
- Se codifica la intención del contenido propio (curiosidad, humor, demostración técnica).
- No se infiere el estado emocional, la vulnerabilidad ni el perfil de quien lo ve.
- emotion, valence y arousal son lectura del autor (coded_by: author), no datos medidos.
- confidence usa low, medium o high.
