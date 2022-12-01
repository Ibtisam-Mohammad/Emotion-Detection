# Fetching the latest node image on apline linux
FROM node:alpine AS production

# Declaring env
ENV NODE_ENV production

# Setting up the work directory
WORKDIR /react-app

# Installing dependencies
COPY ./package.json /react-app
RUN npm install

# Copying all the files in our project
COPY . .

EXPOSE 3000

# Starting our application
CMD npm start
