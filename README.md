# Tereré Tycoon

Juego de tocar para ganar guaraníes, con anuncios recompensados de AdMob.

## Novedades de la versión 5

- **Más vida en el puesto**: unas 200 frases nuevas. Los ayudantes hablan según la hora y la zona, charlan entre ellos y reaccionan cuando comprás, jugás, abrís una canasta, mirás un anuncio o cambiás de zona.
- **Tocar a la gente**: al tocar a un ayudante o a un cliente en la escena contestan y, cada tanto, dejan una propina. En la pestaña Equipo también se puede tocar la cara de cada ayudante.
- **Minijuegos nuevos**: "Ordenar el estante" (cambiar guampas de lugar de la más chica a la más grande, con puntos extra por usar pocos cambios) y "Secuencia de guampas" (repetir la secuencia de luces y sonidos).
- Nueva misión diaria ("Charlá con la gente del puesto") y 3 logros nuevos.

## Cómo se compila

Cada vez que se sube un cambio a la rama `main` (o se ejecuta a mano desde la pestaña **Actions**), GitHub arma el proyecto de Android, compila un APK de prueba y lo publica en **Releases**. Desde el celular se descarga e instala directamente.

## Qué tiene el juego

- **Puesto:** tocar la guampa, mejoras, cofre sorpresa y ganancias x2 (con anuncio).
- **Equipo:** 4 ayudantes con nombre y bonus propios.
- **Juegos:** Hora pico, ruleta diaria, memoria de yuyos y pedidos.
- **Colección:** guampas y yuyos paraguayos que se consiguen en canastas y dan bonus.
- **Metas:** racha diaria, misiones, logros y sucursales (bonus permanente).

## Ambientación (versión 4)

- **Día y noche:** el puesto cambia de cielo, sol, luna y luces según la hora del celular. Para probar otra hora se agrega `?hora=21` a la dirección de la versión web.
- **Música y ambiente:** todo se genera dentro del juego (no hay archivos de audio ni canciones de nadie). La polca cambia con la hora y la zona, y el ambiente suma pájaros, chicharras, grillos y bocinas.
- **Ajustes** (botón de arriba a la derecha): música, efectos, ambiente, volumen y ahorro de batería. El botón del parlante apaga o prende todo de una.
- **Animaciones:** monedas que vuelan al saldo, gotas de tereré, confeti, cartel de zona nueva y pantalla de inicio. Se apagan solas si el celular tiene activado "reducir movimiento".

## Dónde están las cosas

- `www/index.html`: el juego completo. La capa de anuncios está en la sección "Capa de anuncios"; la música en "Sonido"; la escena del puesto en "Escena del puesto".
- `scripts/patch-android.py`: conecta AdMob con el proyecto de Android.
- `.github/workflows/android.yml`: la receta de compilación.

## Anuncios

Ahora usa los IDs de prueba oficiales de Google, así que nunca se muestran anuncios reales ni se generan ingresos. Para pasar a anuncios reales hay que:

1. Cambiar `REWARDED_AD_ID` y poner `ADMOB_TESTING = false` en `www/index.html`.
2. Guardar el ID de la app de AdMob como variable `ADMOB_APP_ID` en el repositorio (Settings → Secrets and variables → Actions → Variables).
