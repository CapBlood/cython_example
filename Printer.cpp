//
// Created by Don Sangre on 04.07.2022.
//

#include "iostream"
#include "Printer.h"

namespace printers {
    Printer::Printer() {}

    void Printer::pprint(int num) {
        std::cout << num;
    }
}