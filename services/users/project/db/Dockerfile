# base image
FROM postgres:11.1-alpine

# run create.sql on initialization
#This sql file added to root document .d, and create our databases 
ADD create.sql /docker-entrypoint-initdb.d
