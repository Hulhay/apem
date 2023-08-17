run:
	python3 -m pytest test/$(target)
# 	make run 					will run all test
#	make run target=stores		will run specific directory

update-dependency:
	python3 -m pipreqs.pipreqs --force