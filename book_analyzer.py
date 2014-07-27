#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'mattdevs'
from analyzer import Analyzer
import codecs

class BookAnalyzerException(Exception):
    pass


class BookAnalyzer(object):

    def __init__(self):
        pass

    def analyze(self, filePath):
        """
            Analyze a file.
            @param filePath Path to the file.
        """
        print("Analyzing book located at: %s" % filePath)
        try:
            with codecs.open(filePath, 'r', 'utf8') as book:
                book_contents = book.read()
        except:
            raise BookAnalyzerException("Error: Unable to read book.")
        analyzer = Analyzer()
        analyzer.process_data(book_contents)
        analyzer.report_results()

if __name__ == "__main__":
    print("Welcome to book analyzer.")
    bookAnalyzer = BookAnalyzer()
    # book_path = input("Please enter a file path to process: ")
    book_path = "tests/data/les_miserable.txt"
    bookAnalyzer.analyze(book_path)

