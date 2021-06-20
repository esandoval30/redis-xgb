FROM redis:latest

# Install  pre-requisites to build RedisAI (wget, git, python3, zip g++,cmake)
RUN apt-get -y update && \
    apt-get install -y git python3 wget unzip g++ build-essential libssl-dev tcl cmake

# Build Redis AI (1.7.1)
WORKDIR /data/
RUN git clone --recursive https://github.com/RedisAI/RedisAI && \
    cd RedisAI && bash get_deps.sh cpu && make -C opt setup && make -C opt build

# Run Redis Server with RedisAI
WORKDIR /data/RedisAI
CMD ["redis-server", "--port","6379", "--loadmodule","/data/RedisAI/install-cpu/redisai.so"]
