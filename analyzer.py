__author__ = 'mattdevs'

class WordInfo(object):

    def __init__(self, word):
        """ Initialize the word. """
        self.word = word
        self.occurrences = 0
        self.increment_counter()

    def increment_counter(self):
        """ Increment the number of occurrences of this word by one. """
        self.occurrences += 1

    def get_occurrences(self):
        return self.occurrences

    def get_word(self):
        return self.word


class AnalyzerException(Exception):
    pass


class Analyzer(object):

    def __init__(self):
        """
            Initialize the analyzer.
        """
        self.word_dict = {}

    def process_word(self, target_str):
        """
            Analyze this word.
            @param target_str The word to analyze.
        """
        target_str = target_str.lower()
        if target_str in self.word_dict:
            self.word_dict[target_str].increment_counter()
        else:
            self.word_dict[target_str] = WordInfo(target_str)

    def process_data(self, data_str):
        """
            Process the data provided.
            @param data_str String representing data to analyze.
        """
        if len(data_str) > 0:
            sanitized_data_str = self.strip_ignored_chars(data_str)
            words_list = sanitized_data_str.split(' ')
            for word in words_list:
                sanitized_word = word.strip()
                if sanitized_word and sanitized_word != '':
                    self.process_word(sanitized_word)
        else:
            raise AnalyzerException("Data provided was not valid: Size of 0.")

    def reset(self):
        """ Reset the analyzer so it can analyze something else. """
        self.word_dict = {}

    def strip_ignored_chars(self, unsanitized_str):
        """
            Strip characters we need to ignore out of the string.
            @param unsanitized_str String that has not been sanitized.
        """
        ignored_characters = [',', '.', '"', '!', '?', ']', '[', '{', '}', '(', ')', ';', '-', '\n', '\r', ':', '*']
        for ignored_character in ignored_characters:
            unsanitized_str = unsanitized_str.replace(ignored_character, ' ')
        return unsanitized_str

    def report_results(self):
        """ Report the results of the analysis. """
        print("Found %d unique words." % len(self.word_dict))
        sorted_results = sorted(self.word_dict.values(), key=lambda x: x.get_occurrences(), reverse=True)
        print("Word counts:")
        for word_info in sorted_results:
            print("%s - %d" % (word_info.get_word(), word_info.get_occurrences()))


if __name__ == "__main__":
    print("Analyzer tests...")
    analyzer = Analyzer()
    analyzer.process_data("foo bar baz foo bar baz")
    analyzer.report_results()
    analyzer.reset()
    analyzer.process_data("The quick brown fox jumped over the lazy dog.")
    analyzer.report_results()
