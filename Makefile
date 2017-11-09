SHELL=/bin/bash

.PHONY: cuberite clang-format client log_render schematic_convert render_view

COMMON_CLIENT_CPP=client/src/block_map.cpp client/src/game_state.cpp client/src/graphics.cpp client/src/packet_writer.cpp client/src/types.cpp client/src/util.cpp client/src/nbt_tag.cpp
COMMON_LOGGING_CPP=logging/src/anvil_reader.cpp logging/src/logging_reader.cpp
COMPILE_FLAGS=-std=c++17 -Wall -Wextra -Werror -O3
LINK_FLAGS=-lglog -lgflags -lz -pthread

all: cuberite client log_render render_view schematic_convert

cuberite:
	cd cuberite && \
	mkdir -p Release && \
	cd Release && \
	cmake -DCMAKE_BUILD_TYPE=RELEASE .. && \
	make -j`nproc`

client:
	cd client && \
	cmake . && \
	make

log_render:
	g++ ${COMPILE_FLAGS} \
		${COMMON_CLIENT_CPP} ${COMMON_LOGGING_CPP} logging/src/log_render.cpp \
		-o bin/log_render \
		${LINK_FLAGS}

render_view:
	g++ ${COMPILE_FLAGS} \
		${COMMON_CLIENT_CPP} ${COMMON_LOGGING_CPP} logging/src/render_view.cpp \
		-o bin/render_view \
		${LINK_FLAGS}

schematic_convert:
	g++ ${COMPILE_FLAGS} \
		${COMMON_CLIENT_CPP} \
		schematic_convert/src/schematic_convert.cpp \
		-o bin/schematic_convert \
		${LINK_FLAGS}

clang-format:
	bin/clang-format
