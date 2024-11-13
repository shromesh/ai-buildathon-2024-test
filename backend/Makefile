# 起動
up:
	docker build -t my-fastapi-app . && docker run -p 80:80 -v ./app:/usr/src/app my-fastapi-app

# 停止
down:
	docker ps -q | xargs docker stop


# 再起動
restart: down up
