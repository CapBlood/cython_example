# distutils: language = c++


cdef extern from "Printer.cpp":
    pass

cdef extern from "Printer.h" namespace "printers":
    cdef cppclass Printer:
        Printer()
        void pprint(int)


cdef class PyPrinter:
    cdef Printer* c_obj

    def __dealloc__(self):
        del self.c_obj

    def __cinit__(self):
        self.c_obj = new Printer()

    def pprint(self, num):
        self.c_obj.pprint(num)
