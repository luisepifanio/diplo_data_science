Experimentos con DataScience en CheckOut y métricas de satisfacción de usuarios...
----

-----

Como sabrán, en todo MercadoLibre generamos datos y metadatos en una forma que incluso nos cuesta darnos cuenta y aprovecharlos.  Y sabiendo que para intentar tomar mejores decisiones necesitamos un mejor análisis de los mismos, esa inquietud maldita me decía “mejor porqué no lo intentas con una difícil”,   entonces me permití compartir con ustedes y jugar con una de esas métricas que resulta particularmente esquiva a nosotros los nerds que tratamos de desarrollar un producto mejor: Métrica de satisfacción de usuario,  aquella esquiva “voz del usuario”
En CheckOut, como en muchas otras partes de ML, contamos con Hotjar como herramienta para poder aproximar qué piensan nuestros usuarios ( incluso éste que nos amenazó con abogados ) sin embargo y quizás debido a su enfoque de como analizar el comportamiento del usuario, nos resulta muy trabajoso ponernos analizar caso por caso y detectar patrones de falla.
Creo que más de una vez vi a Agus o Fede ( por nombrar a escasos ) tratando de decodificar un mesaje oculto en gráficas como las siguientes:

![alt text](https://raw.githubusercontent.com/luisepifanio/diplo_data_science/develop/analysis_and_visualization/tareas_integradoras/img/hotjar4.png "Logo Title Text 1")

Sin embargo, los datos están y Hotjar  tiene api para renderizar los resultados de los “incomming feedbacks”,entonces ( por más que mis compañeros me quieran jubilar y digan que mejor me dedique a los Excel) decidí tirar algunos scripts en groovy ( para los curiosos https://asciinema.org/a/ts8vpl4C9pg50giLqOEmcFiC7 ) y desenroscar los datos de su api y exportarlos de una manera mas aprovechable, eso definitivamente era una oportunidad...
Además, aprovechando la diplomatura en ciencia de datos ( y porque no contradiciendo eso de que “perro viejo no aprende trucos nuevos” ) tomé el enfoque de analizar las tendencias de satisfacción de usuario por cada pantalla del flow de checkout y ver si sacábamos **algo nuevo**. Utilice las herramientas de “la facu”: unas notebooks de Jupyter,  levantar el set de datos que hice con groovy, más algo de horrible código en python. Esto se ve mas o menos así... de simple:

![alt text](https://raw.githubusercontent.com/luisepifanio/diplo_data_science/develop/analysis_and_visualization/tareas_integradoras/img/capturaDeNotebook.jpg "Logo Title Text 1")

Pero la capacidad de enriquecimiento que pueden generar las visualizaciones es sorprendente, por ejemplo hace unos días nos notificaron ”Saben de algunos problemas con Cabal?” entonces fui a la pantalla de **“installments”** y **“payments”** más algunas queries, y lo que se ve en hotjar así:

![alt text](https://raw.githubusercontent.com/luisepifanio/diplo_data_science/develop/analysis_and_visualization/tareas_integradoras/img/mediaXPHOtjar.jpg "Logo Title Text 1")

y teniendo en cuenta que ”las caritas” son escalas del 0 al 4 (siendo que 0 es la queja y lo contrario el 4), en mis notas se ven así

![alt text](https://raw.githubusercontent.com/luisepifanio/diplo_data_science/develop/analysis_and_visualization/tareas_integradoras/img/installmentsBySatisLevel.png "Logo Title Text 1")

O siendo una poco mas binario y definiendo 3 como “oportunidad de mejora” ( y la herramienta eligiendo inoportunamente como rojo ) 

![alt text](https://raw.githubusercontent.com/luisepifanio/diplo_data_science/develop/analysis_and_visualization/tareas_integradoras/img/installmentsByOportunity.png "Logo Title Text 1")

Incluso pude verificar un bug que tuvimos hace unos días en la pantalla de "billing info" ( datos que se usan en facturacion de envios y grandes vendedores ), y que los usuarios efectivamente acusaron quejosamente

![alt text](https://raw.githubusercontent.com/luisepifanio/diplo_data_science/develop/analysis_and_visualization/tareas_integradoras/img/userIdentification.png "Logo Title Text 1")

pero antes que me digas: “y esto que tiene que ver esto con Cabal”...  en algún momento dijimos de hacer un "text mining" sobre un corpus de no sé qué....investigué y salió esto

![alt text](https://raw.githubusercontent.com/luisepifanio/diplo_data_science/develop/analysis_and_visualization/tareas_integradoras/img/wordCloud%20-%20focus%20.png "Logo Title Text 1")

Efectivamente, creo que aquella esquiva “voz del usuario” está, pero la forma de escucharla es un poco diferente, y además la oportunidad de aplicar técnicas de análisis y visualización de datos para mejorar el producto es un oportunidad que vale la pena investigar y seguir aplicando.

Creo que en mis tiempos libres seguiré tratando de realizar este tipo de esfuerzos y aportes para mejorar esta parte de nuestro producto, pero no quería dejar de compartir estos hallazgos con ustedes, y de paso comentarles que estoy tratando de impulsar este enfoque analítico con ustedes.
Por tal motivo voy a estar viendo como organizarme y realizar algunos mini workshops, si les interesa, y si tienen alguna idea compartírmela y ver si juntos aprendemos algo nuevo.

Gracias por llegar a estas líneas y por su atención ;)





