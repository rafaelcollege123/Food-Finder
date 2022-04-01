FROM node:17.4.0-alpine AS build

WORKDIR /app
ADD ./package.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx
EXPOSE 3000
COPY --from=builder /app/build /usr/share/nginx/html