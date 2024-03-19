#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{ 
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, PyTYPE(item)->tp_name);
	}

}
