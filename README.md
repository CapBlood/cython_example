# Описание
В данном репозитории представлен пример импорта кода C++ в Python.

## Этапы реализации
1. Написать код на C++ (например, .cpp и .h).
2. Создать файл [.pyx](PyPrinter.pyx), в котором реализовать обертку вокруг кода C++, а именно сначала добавляем код C++ из cpp с помощью `cdef extern from "Printer.cpp":`, а затем вытащить необходимое объявление класса из h с помощью `cdef extern from "Printer.h" namespace "printers":`.
3. Написать непосредственно обертку с помощью объявления класса `cdef class PyPrinter:`.
4. Создать скрипт установки [setup.py](setup.py).
5. Запустить в терминале [скрипт](build.sh).
6. Создастся файл .so, который затем можно использовать для работы в Python как обычной библиотеки.

## Сборка модуля
Запустить скрипт build.sh.

## Ссылки
- Оригинальная [инструкция](https://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html)