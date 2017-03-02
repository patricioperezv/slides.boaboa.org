% Recopilacion de datos para Medfasee
% Patricio Pérez <pperez@boaboa.org>
% 2 de Marzo de 2017

# Mirada informatica al proyecto Medfase

Desde el punto de vista informatico podemos resumir y abstraer este proyecto como la medicion de multiples fuentes de datos sincronizadas en tiempo real, permitiendo realizar analisis historicos o en tiempo real de los datos recopilados.

Los datos medidos por este proyecto son recopilados por aparatos llamados **PMUs** (Phasor Measurement Unit), estos miden las ondas electricas de una grilla electrica utilizando una fuente comun de sincronizacion temporal (GPS); estos aparatos envian la informacion a una plataforma que concentra y maneja los datos de streaming de syncrofasores y otros datos de series temporales en tiempo real.

El concentrador permite el analisis historico de datos como tambien analisis en tiempo real.

# Que se esta usando?

El concentrador de datos utilizado en este proyecto es de caracter libre y se llama [OpenPDC](https://github.com/GridProtectionAlliance/openPDC).
Hay dos aplicaciones graficas consumiendo los datos producidos por el concentrador, una es Medplot y la segunda es Medplot RT, la diferencia entre ellas es que una muestra datos en tiempo real, mientras que la otra permite analisis de datos historicos, especificando rangos de fechas y otras opciones para acotar el analisis.

# Como consumir datos en tiempo real

El consumo de datos en tiempo real es una opcion cubierta por los desarrolladores de _OpenPDC_, se debe realizar mediante el **Gateway Exchange Protocol** (Ver [este pdf](https://www.gridprotectionalliance.org/docs/products/gsf/gep-overview.pdf) para una introduccion al protocolo), este basicamente provee un modelo de publicacion/suscripcion y tiene disponibles librerias que permiten el consumo en un par de lenguajes de programacion (Segun lo visto, Java y C#).

Este protocolo puede verse en accion directamente en _OpenPDC_, o en el programa de pruebas: [GEP Subscription Tester](https://github.com/GridProtectionAlliance/openPDC/blob/master/Source/Documentation/wiki/GEP_Subscription_Tester.md), este ultimo esta escrito en C# con la libreria [Time-Series Library o TSL](https://github.com/GridProtectionAlliance/gsf/tree/master/Source/Libraries/GSF.TimeSeries) contenida en [GSF](https://github.com/GridProtectionAlliance/gsf)(Grid Solutions Framework).

## Notas de pato

* Para utilizar el _GEP Subscription Tester_ y no dejar la escoba con la extraccion de datos en Amazon, se debe agregar un segundo output udp en _OpenPDC_.
* El codigo del tester se encuentra en [Github](https://github.com/GridProtectionAlliance/gsf/tree/master/Source/Applications/DataSubscriberTest).

* _GSF_ contiene muchos componentes aparte de la libreria de serie temporal, pudiendo con esta realizar modulos de alarmas, deteccion de datos incorrectos y acceso a datos historicos.

# Consumo de datos en tiempo "casi" real

Para casos de uso que no requieran un nivel de precision tan alto, se puede consumir servicios REST (Basicamente retorna json o xml), algunos endpoints pueden verse en el [wiki de OpenPDC](https://github.com/GridProtectionAlliance/openPDC/blob/master/Source/Documentation/wiki/Getting_Started.md#time-series-web-service).

# Consumo de datos historicos

En este caso se pueden utilizar dos accesos, el servicio REST mencionado en el apartado anterior, o el API "Historian", dando mas opciones a la hora de filtrar y manipular datos.

# Estrategia para recopilar datos fuera de OpenPDC

Si bien OpenPDC en conjunto con las librerias GSF pueden ser utilizadas para construir aplicaciones que muestren, manipulen e incluso reaccionen en funcion de los datos, personalmente pienso que hay herramientas especializadas y mas sencillas de usar, pudiendo utilizarlas ya sea como sistemas de produccion o prototipar con ellas; la recopilacion de datos se ha masificado y hay varias alternativas a la hora de manejar datos de series temporales, entre ellas encontramos el stack **TICK**, este conjunto de aplicaciones trabaja en conjunto para proveer almacenamiento de datos de series temporales, graficos de estos e incluso reactividad ante eventos descritos por el usuario.

Con esa previa en mente, es posible utilizar la libreria TSL para consumir los datos en tiempo real desde OpenPDC e inyectarlos al stack TICK (Precisamente al motor de datos de series temporales **InfluxDB**) mediante su API REST para luego utilizar herramientas como [Grafana](http://grafana.org/) para construir dashboards con graficos en tiempo real o [Kapacitor](https://github.com/influxdata/kapacitor) para gatillar alertas en caso que ciertos umbrales (definidos por el usuario/desarrollador) sean pasados.