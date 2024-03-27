# Build Stage
FROM node:14 as build-stage

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# Development Stage
FROM node:14 as development-stage

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "start"]

# Production Stage
FROM nginx:alpine as production-stage

COPY --from=build-stage /app/build /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/conf.d/

EXPOSE 5173

CMD ["nginx", "-g", "daemon off;"]
