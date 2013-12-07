help:
	@echo Usage: make [\TARGET\]
	@echo
	@echo TARGET:
	@echo "    clean    清理临时文件"
	@echo "    view     view"
	@echo "    test     test"
	@echo "    start    start"
	@echo "    deploy   deploy"
	@echo

.PHONY: clean docs test start deploy

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '*.log' -exec rm -f {} +

view:
	python -m SimpleHTTPServer 8004

build:
	lessc -x --yui-compress static/less/ande.less > static/css/ande.css

test:
	@echo "starting test"
	python hello.py -t

start:
	make test
	@echo "starting"
	python hello.py

deploy:
	@echo "starting deploy"
	git push origin master
	git push pro master
