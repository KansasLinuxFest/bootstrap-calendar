# this is a plugin for pelican
import os.path
import os
#import pelican.contents
from pelican import signals
from pelican.utils import (copy, process_translations, mkdir_p, DateFormatter,
                           FileStampDataCacher, python_2_unicode_compatible)
import shutil
import logging
import os


logger = logging.getLogger(__name__)
class Blah(object):
    def __init__(self, source_path=None):
        self.source_path = source_path


FILES = {
    "css/calendar.min.css" : "css/calendar.min.css",
    'components/bootstrap3/css/bootstrap.min.css' : 'css/bootstrap.css',
    'index.html' : 'calendar.html',
    'components/bootstrap3/css/bootstrap-theme.min.css' : 'css/bootstrap-theme.min.css',
    "components/jquery/jquery.min.js" : "js/jquery.min.js" ,
    "components/underscore/underscore-min.js": "js/underscore-min.js",
    "components/bootstrap3/js/bootstrap.min.js" : "js/bootstrap.min.js",
    "components/jstimezonedetect/jstz.min.js" : "jstz.min.js",
    "js/calendar.js": "js/calendar.js",
    "js/app.js": "js/app.js",
}

def register(pelican):
    """
    now we register this plugin into pelica
    """



    #pelican.context['staticfiles'].append(sc)

class StaticGenerator(object):
    """
    new class for going custom generation for this class
    """
    def __init__(self, pelican=None, path=None, theme=None, output_path=None, context=None, settings=None):
        self.pelican=pelican
        self.path = path
        self.output_path = output_path
        #signals.static_generator_init.send(self)

    def generate_aticles(self, write):
        signals.article_generator_write_article.send(self, content=article)

    def generate_context(self):
        print 'gen context'

    def generate_output(self, writer):
        print 'gen output'

        curpath = os.path.dirname(__file__)

        # copy all Static files
        for sc in FILES.keys():
            target = FILES[sc]
            basename = os.path.basename(sc)
            source_path = os.path.join(curpath, sc)
            save_as = os.path.join(self.output_path, target)
            logger.info('Going to Copy %s to %s', sc, save_as)
            mkdir_p(os.path.dirname(save_as))
            shutil.copy2(source_path, save_as)
            logger.info('Copying %s to %s', sc, save_as)

def get_generators(pel):
    return StaticGenerator
   
