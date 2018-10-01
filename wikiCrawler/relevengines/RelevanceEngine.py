from re import match

class RelevanceEngine(object):

    def __init__(self, dict_location, search_terms):
        self.words = []
        self.search_terms = search_terms

        # Build and init a list of words which will be the ones we care about
        # I.E, for 'green' get all the words in the dict with green in them
        try:
            file = open(dict_location, 'r')
            for line in file:
                to_include = False
                for term in search_terms:
                    if match('.*' + term.lower() + '.*', line):
                        to_include = True
                if to_include:
                    self.words.append(line.lower().strip())

        except IOError:
            print("Couldn't open the dict for writing for some reason")
            exit(1)


    def is_url_relevant(self, url):
        if len(self.search_terms) == 0:
            return True  # No search terms means get anything

        #Break url up into words, then check if any of those words are in our relevant list
        try:
            end_url = match('.*wiki/(.*)', url).group(1)
            end_url = end_url.lower()
            words_in_url = end_url.split('_')
            for lookup_word in words_in_url:
                for reference_word in self.words:
                    if lookup_word == reference_word:
                        return True
        except:
            return False  # Url didn't even match expected URL format, definitely not relevant

        return False

    def is_text_relevant(self, some_text):
        if len(self.search_terms) == 0:
            return True  # No search terms means get anything

        # Do some preprocessing
        some_text = some_text.lower()
        some_text.replace('.', '')
        some_text.replace('!', '')
        some_text.replace('&', '')
        some_words = some_text.split(' ')

        for lookup_word in some_words:
            for reference_word in self.words:
                if lookup_word == reference_word:
                    return True
        return False

if __name__ == '__main__':
    # Some manual tests
    myeng = RelevanceEngine('../resource/words.txt', ['green'])
    print(myeng.is_text_relevant('His this is not'))
    print(myeng.is_text_relevant('This GreEn text is'))
    print(myeng.is_text_relevant('my greenhouse also is'))
    print(myeng.is_text_relevant('The dumbgreen is not though'))

    print(myeng.is_url_relevant('/wiki/this_is_green'))
    print(myeng.is_url_relevant('/wiki/Greenhouse_gasses'))
    print(myeng.is_url_relevant('/wiki/not_a_very_7green_url'))
    print(myeng.is_url_relevant('/wiki/neither_is_this_green6'))