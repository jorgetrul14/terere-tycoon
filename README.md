# Tereré Tycoon

Juego de tocar para ganar guaraníes, con anuncios recompensados de AdMob.

## Cómo se compila

Cada vez que se sube un cambio a la rama `main` (o se ejecuta a mano desde la pestaña **Actions**), GitHub arma el proyecto de Android, compila un APK de prueba y lo publica en **Releases**. Desde el celular se descarga e instala directamente.

## Qué tiene el juego

- **Puesto:** tocar la guampa, mejoras, cofre sorpresa y ganancias x2 (con anuncio).
- **Equipo:** 4 ayudantes con nombre y bonus propios.
- **Juegos:** Hora pico, ruleta diaria, memoria de yuyos y pedidos.
- **Colección:** guampas y yuyos paraguayos que se consiguen en canastas y dan bonus.
- **Metas:** racha diaria, misiones, logros y sucursales (bonus permanente).

## Dónde están las cosas

- `www/index.html`: el juego completo. La capa de anuncios está en la sección "Capa de anuncios".
- `scripts/patch-android.py`: conecta AdMob con el proyecto de Android.
- `.github/workflows/android.yml`: la receta de compilación.

## Anuncios

Ahora usa los IDs de prueba oficiales de Google, así que nunca se muestran anuncios reales ni se generan ingresos. Para pasar a anuncios reales hay que:

1. Cambiar `REWARDED_AD_ID` y poner `ADMOB_TESTING = false` en `www/index.html`.
2. Guardar el ID de la app de AdMob como variable `ADMOB_APP_ID` en el repositorio (Settings → Secrets and variables → Actions → Variables).
