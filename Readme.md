version: "3.4"
x-environment:
  &default-environment
  DATABASE_URL: postgres://postgres:postgres@postgres:5432/postgres
  SECRET_KEY: 747dbf22622bb87955856a4f607998d24e5a2ba01e16ea551e0cf5176fe47ce5
  PORT: 8000
  EMAIL_URL: smtp://email:password@smtp_url:port # https://glitchtip.com/documentation/install#configuration
  GLITCHTIP_DOMAIN: https://nslog.neuroticsolutions.com
  DEFAULT_FROM_EMAIL: leyendanerd@gmail.com
x-depends_on:
  &default-depends_on
  - postgres
  - redis

services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_HOST_AUTH_METHOD: "trust"
    restart: unless-stopped
    volumes:
      - pg-data:/var/lib/postgresql/data
  redis:
    image: redis
    restart: unless-stopped
  web:
    image: glitchtip/glitchtip
    depends_on: *default-depends_on
    ports:
      - "8000:8000"
    environment: *default-environment
    restart: unless-stopped
  worker:
    image: glitchtip/glitchtip
    command: ./bin/run-celery-with-beat.sh
    depends_on: *default-depends_on
    environment: *default-environment
    restart: unless-stopped
  migrate:
    image: glitchtip/glitchtip
    depends_on: *default-depends_on
    command: "./manage.py migrate"
    environment: *default-environment

volumes:
  pg-data: