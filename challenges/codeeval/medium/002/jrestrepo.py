#!/usr/bin/python3
"""Codeval challenge17"""


def get_tests():
    """Get data"""
    casos = []
    with open("sys.arg[0]", "r") as insumos:
        for indice in insumos:
            casos.append(indice.strip())
    return casos


def main():
    """main function"""
    tests = get_tests()
    data = {}
    phrase = int(tests[0])
    for test in tests:
        data[len(test)] = test
    for indice in range(phrase):
        print data[max(data)]
        del data[max(data)]


main()
