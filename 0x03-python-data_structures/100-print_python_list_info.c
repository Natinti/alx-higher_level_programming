#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function that print basic info about python lists
 * @p: python list
 */

void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*} Size of the Python List = %lu\n",Py_SIZE(p));
	printf("[*] Allocated = %lu\n", obj->allocated);
	for (i = 0; i < PY_SIZE(p); i++)
		printf("Element %d: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
