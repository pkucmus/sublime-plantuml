FROM java

MAINTAINER Pawel Kucmus <pkucmus@gmail.com>

RUN apt-get update && apt-get install -y --no-install-recommends graphviz

ADD plantuml.jar plantuml.jar

ENTRYPOINT ["java", "-jar", "plantuml.jar"]
CMD ["-nbthread", "auto", "-pipe"]
