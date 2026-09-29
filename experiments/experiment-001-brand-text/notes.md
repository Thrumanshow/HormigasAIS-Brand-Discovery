# Experimento 001: texto de marca en pantalla (H2)

## Variable
Duración del texto `#HormigasAI` en el video.
- A: sin texto
- B: 3-5 s
- C: todo el video

## Constantes
Tema, duración, audio, primer fotograma, caption, hashtags, hora, cuenta.

## Hashtags fijos
- YouTube: @chriswarriortv #HormigasAI #chriswarriortv #trendingonshorts #fyp #Suscribete
- Instagram: @Hormigas-ai #HormigasAI #trendingreels #instagram #Suscribete

## Ventanas de medición
1 h, 24 h, 72 h, 7 d (una fila por medición en data/registro.csv)

## Métrica principal
non_follower_reach, seguida de profile_visits y new_followers.

## Limitaciones
Un video por variante en esta ronda: las diferencias pueden ser ruido.
Repetir 3-5 rondas rotando el orden antes de concluir.

## Pendiente
- Experimento 002: etiquetas #apna... con vs. sin.

## Video base
- Tema: A16@Soberano:~/HormigasAIS-Brand-Discovery (prompt de la terminal)
- Duración (s): menos de 14 (valor exacto pendiente)

## Nota de diseño
El prompt de la terminal muestra "HormigasAIS" en pantalla en las tres
variantes. Variante A (control): no añade texto de marca, hashtag ni sticker en edición; conserva solo los elementos originales del video (incluido el prompt).
