# Estabilidad-de-Talud-aplicacion-del-metodo-de-Fellenius-en-py
Método Fellenius/Petterson
En este método se asumen superficies de falla circulares, se divide el área de falla en dovelas o bloques verticales, posteriormente se obtienen las fuerzas actuantes y resultantes para cada dovela, y finalmente con la sumatoria de estas fuerzas se estima el factor de seguridad (FS). Las fuerzas actuantes sobre una dovela son:

El peso, el cual se puede descomponer en una tangente y una normal a la superficie de falla.
Las fuerzas resistentes de cohesión y fricción que actúan en forma tangente a la superficie de falla.
Las fuerzas de presión de tierras y cortante sobre las paredes entre dovelas (las cuales no son tomadas en cuenta en el método de Fellenius).



Información del terreno
En la siguiente figura se observan las dimensiones y geometría del talud que se estará analizando:
Dimensiones y geometría del talud analizado en GEO5
Figura 1: Dimensiones y geometría del talud analizado

Para nuestro ejemplo, disponemos de la siguiente información del terreno:

Tabla 1: Datos del terreno

Información

Dato

Tipo de suelo: arcilla arenosa

SC

Peso unitario saturado (PU):

18.50 kN/m³

Peso unitario saturado (PUsat):

19.50 kN/m³

Cohesión (c):

21 kPa

Ángulo de fricción interna (Φ):

27º

Método Fellenius/Petterson
En este método se asumen superficies de falla circulares, se divide el área de falla en dovelas o bloques verticales, posteriormente se obtienen las fuerzas actuantes y resultantes para cada dovela, y finalmente con la sumatoria de estas fuerzas se estima el factor de seguridad (FS). Las fuerzas actuantes sobre una dovela son:

El peso, el cual se puede descomponer en una tangente y una normal a la superficie de falla.
Las fuerzas resistentes de cohesión y fricción que actúan en forma tangente a la superficie de falla.
Las fuerzas de presión de tierras y cortante sobre las paredes entre dovelas (las cuales no son tomadas en cuenta en el método de Fellenius).
En nuestro “Curso en Estabilidad de Taludes y Diseño Sismorresistente de Muros, Pantallas y Excavaciones” se discute a mayor profundidad este y otros métodos de análisis para analizar la estabilidad de taludes.

Metodo ordinario o de Fellenius 1927
Figura 2: Método ordinario o de Fellenius (1927).

El factor de seguridad viene expresado de la siguiente manera:


Donde:

ui : Presión de poros entre bloques
ci , φi : Valores efectivos de parámetros de suelos
Wi : Peso del bloque
Ni : Fuerza normal a lo largo del segmento de la superficie de deslizamiento
αi : Inclinación del segmento de la superficie de deslizamiento
li : Longitud de la superficie de deslizamiento
Para nuestro caso planteamos una superficie de deslizamiento determinada por una circunferencia con centro en O=[x,z]=[13.5279;19.9443] y un radio R=15.00m. El talud fue dividido en dovelas verticales con un ancho b=1.0m quedando un total de 20 dovelas conformadas:

Definición de bloques de análisis para el talud
Figura 3: Definición de dovelas verticales para el análisis del talud

Se debe determinar el área de las dovelas según se encuentren por encima (Ai) o por debajo (Bi) del nivel freático; una vez calculadas estas áreas se procede a calcular el peso de las dovelas individuales y el peso total. Para ello utilizaremos las siguientes expresiones:


En la siguiente tabla se muestran los resultados obtenidos para todos las dovelas/bloques:

Fuerzas obtenidas para cada dovela vertical
Tabla 2: Fuerzas obtenidas para cada dovela/bloque

Inclinación de la superficie de deslizamiento para cada dovela y presión de poros
A modo de simplificar el cálculo manual, se opta por convertir las curvas de la superficie de deslizamiento en líneas; la inclinación se determina según el ángulo entre la superficie de deslizamiento y el plano horizontal:

Inclinación de la superficie de deslizamiento para cada bloque y presión de poros
Figura 4: Inclinación de la superficie de deslizamiento para cada bloque y presión de poros

La longitud de la superficie de deslizamiento para cada bloque vendría de la siguiente expresión:


La altura del nivel freático se toma como la longitud que existe entre la superficie de deslizamiento y el nivel freático medido desde el centro de la dovela en cuestión:

Altura del nivel freático para el análisis
Figura 5: Altura del nivel freático para el análisis

La reducción de altura del nivel freático se obtiene de la siguiente expresión:


La expresión para calcular la presión de poros:


Finalmente se obtienen las fuerzas horizontales de la presión de poros con la expresión:


En las siguientes tablas se muestran los resultados para todas las dovelas/bloques:


Tabla 3-1: Fuerzas horizontales de la presión de poros para cada dovela (Parte 1)


Tabla 3-2: Fuerzas horizontales de la presión de poros para cada dovela (Parte 2)

Momento deslizante para análisis del Talud
Se estima a partir del peso de las dovelas individuales incluyendo las fuerzas de la carga actuante sobre el tramo horizontal desde el eje de la dovela hasta el centro de la superficie de deslizamiento. El brazo es calculado desde el inicio de la superficie de deslizamiento (Z=[x,z]=[8.00;5.00]).

La expresión para calcular el brazo es la siguiente:


Y para el momento deslizante tenemos:


En la siguiente tabla se muestran los resultados para todas las dovelas/bloques:

Resultados de Momento deslizante para cada dovela
Tabla 4: Resultados de Momento deslizante para cada dovela

Fuerza activa resultante:

Momento resistente para análisis del talud (Fellenius)
Se calculan las fuerzas normales de cada dovela individual. La fuerza normal actúa verticalmente sobre la superficie de deslizamiento.

Cálculo de la fuerza normal:


Cálculo del momento resistente:


En la siguiente tabla se muestran los resultados para todas las dovelas/bloques:

Resultados de Momento resistente para cada dovela
Tabla 5: Resultados de Momento resistente para cada dovela

Fuerza activa resultante:

Factor de seguridad:

Comparativa con GEO5 (Talud sin Anclaje)
A continuación se presentan los resultados obtenidos en el Módulo Estabilidad de Taludes del software GEO5 utilizando el Método de Fellenius. Se observa que el análisis de estabilidad del talud es NO ACEPTABLE, tal como se ha determinado de forma manual.

Comparativa con GEO5_Sin anclaje
Figura 6: Resultados de análisis del Talud en GEO5 (sin considerar anclaje) aplicando el Método de Fellenius

Verificación de estabilidad del Talud con anclaje
Debido a que no se obtuvo un FS satisfactorio, se optará por reforzar el talud con el uso de anclajes. Se utilizará un anclaje con fuerza FA=200 kN y un espaciamiento bA=2.00 m. La cabeza del anclaje se ubica en HA=[x,z]=[16.00;9.00] (ubicado en la dovela/bloque #9):

Dimensiones y geometría del talud con anclaje
Figura 7: Dimensiones y geometría del talud con anclaje

Se determinan las fuerzas y momento resistente del anclaje:

Fuerza por metro del anclaje:

Cálculo del brazo de la fuerza de anclaje:

Momento resistente del anclaje:

Se procede a actualizar la tabla de momentos resistentes con el aporte del anclaje para la dovela #9:

Resultados de Momento resistente considerando anclaje
Tabla 6: Resultados de Momento resistente considerando anclaje

Los resultados para el análisis del Talud con anclaje serán:

Momento resistente total:

Fuerza pasiva resultante:

Factor de seguridad:

Comparativa con GEO5 (Talud con Anclaje)
A continuación se presentan los resultados obtenidos en el Módulo Estabilidad de Taludes del software GEO5 utilizando el Método de Fellenius. Se observa que el análisis de estabilidad del talud es ACEPTABLE luego de reforzar el talud con el anclaje.

Comparativa resultados de análisis del Talud con Anclaje en GEO5
Figura 8. Comparativa resultados de análisis del Talud con Anclaje en GEO5 (Método de Fellenius)

Método simplificado de Bishop
Este método se desarrolla mediante el equilibrio de momentos y equilibrio de fuerzas verticales de cada una de las franjas en que se divide la superficie de falla. Sin embargo, para las franjas individuales, ni los momentos ni los equilibrios de fuerzas horizontales son satisfechos.

Aunque las condiciones de equilibrio no se satisfacen completamente, este método es un procedimiento satisfactorio y el más recomendable cuando la superficie de falla es circular.

En nuestro “Curso en Estabilidad de Taludes y Diseño Sismorresistente de Muros, Pantallas y Excavaciones” se discute a mayor profundidad este y otros métodos de análisis para analizar la estabilidad de taludes.

Método simplificado de Bishop 1955
Figura 9: Método simplificado de Bishop (1955).

La superficie de deslizamiento es la misma que en el primer cálculo utilizando el Método de Fellenius (Figura 3). El cálculo del peso de los bloques individuales se muestra en la Tabla 2. Por lo cual, se utilizará el Momento deslizante (Ma) calculado previamente. 

Momento resistente para análisis del talud (Bishop)
El cálculo de los momentos resistentes (Mp) es iterativo, ya que el mismo depende del factor de seguridad. Para la primera iteración se considera un FS=1.50 y a partir de allí se realizan 3 iteraciones adicionales.

Factor de seguridad:

Momento resistente:

En la siguiente tabla se muestran los resultados de las iteraciones:

Resultados de Momento resistente para cada iteración_Método Bishop
Tabla 7: Resultados de Momento resistente para cada iteración (Método Bishop)

Los resultados para el análisis del Talud aplicando el Método de Bishop serán:

Momento resistente: Mp = 16019.33 kN/m
Factor de seguridad: FS = 1.535
Comparativa con GEO5 (Talud sin Anclaje)
A continuación se presentan los resultados obtenidos en el Módulo Estabilidad de Taludes del software GEO5 utilizando el Método de Bishop. Se observa que el análisis de estabilidad del talud es ACEPTABLE.

Comparativa con GEO5 Bishop_Sin anclaje
Figura 10: Comparativa resultados de análisis del Talud en GEO5 (sin considerar anclaje) (Método Bishop)

Verificación de estabilidad del Talud con anclaje
Se evalúa el talud reforzado con anclaje con la finalidad de comparar con los resultados obtenidos aplicando el Método de Fellenius.

Resultados de Momento resistente considerando anclaje_Metodo Bishop
Tabla 8: Resultados de Momento resistente considerando anclaje (Método Bishop)

Los resultados para el análisis del Talud con Anclaje aplicando el Método de Bishop serán:

Momento resistente: Mp = 17210.85 kN/m
Factor de seguridad: FS = 1.650
Comparativa con GEO5 (Talud con Anclaje)
A continuación se presentan los resultados obtenidos en el Módulo Estabilidad de Taludes del software GEO5 utilizando el Método de Bishop. Se observa que el análisis de estabilidad del talud continua siendo ACEPTABLE luego de reforzar el talud con el anclaje.

Comparativa con GEO5 Bishop_Con anclaje
Figura 11: Comparativa resultados de análisis del Talud con anclaje en GEO5 (Método Bishop)

Conclusiones
Al efectuar el análisis de estabilidad de taludes mediante el método de Fellenius/Petterson, el factor de seguridad (FS) obtenido arrojó resultados más conservadores que el método de Bishop, resultando la verificación desfavorable para el primer caso y favorable para el segundo.
El refuerzo mediante anclajes propuesto resultó ser una solución adecuada para incrementar el factor de seguridad obtenido inicialmente.
La confiabilidad de los resultados obtenidos por el software está respaldada por la verificación manual realizada, por lo que el análisis a través del uso de softwares de cálculo se presenta como una propuesta fiable y óptima que puede ahorrarnos mucho tiempo a la hora de realizar análisis en proyectos más grandes o complejos, con evaluación simultánea de cientos de superficies probables de falla, pudiendo efectuar la verificación mediante diferentes métodos. También nos facilita la posibilidad de comparar de una manera más automatizada entre diferentes propuestas de refuerzo y evaluar varias etapas de construcción.
El análisis y verificación de la estabilidad de taludes forma parte del contenido de nuestro “Curso en Estabilidad de Taludes y Diseño Sismorresistente de Muros, Pantallas y Excavaciones”, donde se discuten y comparan los resultados obtenidos mediante la aplicación de diferentes métodos de análisis, se desarrollan cuantiosos ejemplos de cálculo para diferentes escenarios y se validan los resultados contra softwares de cálculo como el GEO5 (Fine Software), que ha servido de herramienta de validación en el presente artículo.

Referencias
• Petterson KE (1955) The early history of circular sliding surfaces. Geotechnique 5:275–296.

•Bishop, A.W. (1955) "The Use of the Slip Circle in the Stability Analysis of Slopes", Geotechnique, Great Britain, Vol. 5, No. 1, Mar., pp. 7-17.

•https://www.finesoftware.es/ayuda-en-linea/geo5/es/analisis-05/
