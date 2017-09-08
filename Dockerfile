FROM haproxy:1.7

RUN useradd haproxy
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
#
