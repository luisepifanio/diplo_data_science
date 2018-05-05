Contexto y Proposito Laboratorio 2
---

El contexto del segundo laboratorio estará ( o estuvo ya que fue presentado según quiera verse ) basado en la necesidad de una empresa en conocer *tendencias en métricas de satisfaccion de usuario*

Actualmente la companía en que trabajo ( MercadoLibre ) cuenta con una tool llamada "Hotjar" para realizar el analisis de las tendencias de satisfaccion de usuario, la cual cuenta con la posibilidad de incluir un widget html, que levanta un formulario

Siendo gráficos esto durante el flujo de compras, en el que trabajo, se ve así

![alt text](https://raw.githubusercontent.com/luisepifanio/diplo_data_science/develop/analysis_and_visualization/tareas_integradoras/img/hotjar1.png "Logo Title Text 1")


![alt text](https://raw.githubusercontent.com/luisepifanio/diplo_data_science/develop/analysis_and_visualization/tareas_integradoras/img/hotjar2.png "Logo Title Text 1")

Y su importancia radica en que nos permite priorizar y detectar las oportunidades de mejoras sobre la usabilidad y diseño de la aplicacion

Sabiendo que no podemos hacer pruebas con usuarios o contactarlos para contactarles como fue su experiencia de compra, la idea para el Laboratorio 2 fue, quizás escueto, poder demostrar las ventajas del analisis y visualización de los datos y como plus tambien poder utilizarlo para detectar oportunidades en principio.

Como referencia, Hotjar para realizar el analisis de lo datos que recolectamos tiene 2 vistas. La primera para recorrer cada comentario:

![alt text](https://raw.githubusercontent.com/luisepifanio/diplo_data_science/develop/analysis_and_visualization/tareas_integradoras/img/hotjar3.png "Logo Title Text 1")

Lo cual resulta poco efectivo cuando llegan a veces 400 comentarios diarios por plataforma ( web desktop y web mobile ) y es muy trabajoso

Y por otro lado, brinda un promedio global de experiencia del usuario, lo cual si bien es mejor que nada, no nos permite analizar el paso a paso de la aplicación

![alt text](https://raw.githubusercontent.com/luisepifanio/diplo_data_science/develop/analysis_and_visualization/tareas_integradoras/img/hotjar4.png "Logo Title Text 1")

Por tal motivo el objetivo fue, quizas escueto, pero poder demostrar que se pudieron trazar incidentes productivos, en nuestro caso 2:

- Problemas en la carga de DNI: Para esto basto con contar la cantidad de incidentes en la pantalla y mostrar a los responsables de experiencia de usuario que pudimos, efectivamente, medir este evento
- Problemas con el uso de tarjeta Cabal en el flow de pagos al dar de alta la tarjeta: Aqui utilizamos una visualización "Word Cloud", donde "Cabal" se muestra como un foco de atención

Esto fue llevado a cabo mostrando la notebook de Jupyter en vivo en una reunión con los responsables de producto de ML y terminó en un post en el blog técnico interno de la compañia ( utilzamos facebook at work, una version empresarial de facebook ) que intentare subir como parte del laboratorio, y como plan de acción empezamos con una capacitacion interna en las herramientas que vimos en este curso ( del cual me llevo el dudoso honor de dirigir ;= )

Por otra parte, dejo un dataset reducido a 100 entradas porque, primero es muy pesado ( sacar los datos de las apis de hotjar me llevo 195 MB de json y unos 90 de csv ) y ademas porque desconozco la privacidad de los datos, sin embargo me llevo el tema de dejar el dataset de la semana en analisis a disposición

