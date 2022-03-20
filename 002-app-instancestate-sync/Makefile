BINARY_NAME=synctest
BINARY_SRC_DIR=./cmd/synctest
BUILD_DIR=./build
TEST_SRC_DIRS=./cmd/synctest/ ./internal/synctest/

GOARCH=amd64
ifeq ($(OS), Windows_NT)
    GOOS := "windows"
else
    GOOS := $(shell uname | tr '[:upper:]' '[:lower:]')
endif

format:
	@echo "🧹 Formatting source code..."
	@gofmt -e -l -w ./cmd/synctest/
	@gofmt -e -l -w ./internal/synctest/
# 	@gofmt -e -l -w ./tools/
	@echo ""

test: ${TEST_SRC_DIRS}
	@echo "🧑‍🏫 Running tests..."
	@set -e; for crnt_source_dir in ${TEST_SRC_DIRS}; do go test $${crnt_source_dir}; done;
	@echo ""

build: format test
	@echo "🏗  Building ${BINARY_NAME} executable..."
	@set -e; go build -o ${BUILD_DIR}/${BINARY_NAME}-$(GOOS) ${BINARY_SRC_DIR}/main.go
	@echo ""
	@echo "🙋 Use \`make run\` to run the executable"
	@echo "🤓 Use \`make out\` to show where to find the executable"

run:
	@${BUILD_DIR}/${BINARY_NAME}-$(GOOS)

out:
	@echo "🦔 Runnable Excutable is here: ${BUILD_DIR}/${BINARY_NAME}-$(GOOS)"

clean:
	go clean
	rm ${BUILD_DIR}/${BINARY_NAME}-$(GOOS)

.PHONY: build clean format out run test
