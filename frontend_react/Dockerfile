# Fetching the latest node image on apline linux
FROM node:alpine AS production

# Declaring env
ENV NODE_ENV production

# Setting up the work directory
WORKDIR /react-app
RUN apk add sudo && sudo apk update
# Installing dependencies
COPY ./package.json /react-app
RUN npm install

# Copying all the files in our project
COPY . .
RUN echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p

EXPOSE 3000

# Starting our application
CMD npm start
