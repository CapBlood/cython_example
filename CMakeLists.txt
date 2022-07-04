cmake_minimum_required(VERSION 3.20)
project(cython)

set(CMAKE_CXX_STANDARD 14)

add_executable(cython main.cpp Printer.cpp Printer.h)
