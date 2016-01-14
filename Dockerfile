FROM java

MAINTAINER Pawel Kucmus <pkucmus@gmail.com>

ADD plantuml.jar plantuml.jar

ENTRYPOINT ["java", "-jar", "plantuml.jar"]
CMD ["-nbthread", "auto", "-pipe"]
