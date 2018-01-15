#!/usr/bin/python
#filename:kgp.py

from xml.dom import minidom
import random
import toolbox
import sys
import getopt

_debug=0

class NoSourceError(Exception):pass
class KantGenerator:
    '''generates mock philosophy based on a context-free grammar'''
    def __init__(self, grammar, source=None):
        self.loadGrammar(grammar)
        self.loadSource(source and source or self.getDefaultSource())
        self.refresh()
    def _load(self, source):
        '''load XML input source, return parsed XML document
        -a URL of a remote XML file ("http://diveintopythonorg/kant.xml")
        -a filename of local XML file ("/diveintopython/common/py/kant.xml")
        - standard input ("-")
        - the actual XML document, as a string
        '''
        sock = toolbox.openAnything(source)
        xmldoc = minidom.parse(sock).documentElement
        sock.close()
        return xmldoc
    def loadGrammar(self, grammar):
        '''load context-free grammar'''
        self.grammar = self._load(grammar)
        self.refs = {}
        for ref in self.grammar.getElementsByTagName("ref"):
            self.refs[ref.attributes["id"].value]=ref

    def loadSource(self, source):
        '''load source'''
        self.source = self._load(source)

    def getDefaultSource(self):
        '''guess default source of the current grammar
        The default source will be one of the <ref>s thas is not
        cross-referenced. This sounds complicated but it's not.
        Example: the default source for kant.xml is
        "<xref id='section'/>", because'section' is the one <ref>
        thas is not <xref>'d anywhere in the grammar.getElementsByTagName
        In most grammars,the default source will produce the
        longest(ant most interesting) output.
        '''
        xrefs = {}
        for xref in self.grammar.getElementsByTagName("xref"):
            xrefs[xref.attributes["id"].value]=1

        xrefs=xrefs.keys()
        standaloneXrefs=[e for e in self.refs.keys() if e not in xrefs]
        if not standaloneXrefs:
            raise NoSourceError, "can't guess source, and no source specified."
        return '<xref id="%s"/>' % random.choice(standaloneXrefs)
    def reset(self):
        '''reset parser'''
        self.pieces=[]
        self.capitalizeNextWord = 0

    def refresh(self):
        '''reset output buffer, re-parse entire source file, and return output
        Since parsing involves a good deal of randomness, this is an
        easy way to get new output without having to reload a grammar file
        each time.
        '''
        self.reset()
        self.parse(self.source)
        return self.output()
    def output(self):
        '''output generated text'''
        return "".join(self.pieces)
    def randomChildElement(self, node):
        '''choose a random child element of a node
        This is a utility method used by do_xref and do_choice.
        '''
        choices = [e for e in node.childNodes
                   if e.nodeType == e.ELEMENT_NODE]
        chosen=random.choice(choices)
        if _debug:
            sys.stderr.write('%s available choices: %s\n' % \
                             (len(choices), [e.toxml() for e in choices]))
            sys.stderr.write('Chosen:%s\n' % chosen.toxml())

        return chosen
    def parse(self, node):
        '''parse a single XML node
        A parsed XML document is a tree of nodes
        of various types. Each node is represented by an instance of the
        corresponding Python class(Element for a tag, Text for
        text data, Document for the top-level document).The following
        statement constructs the name of a class method based on the type
        of node we're parsing ("parse_Element" for an Element node,
        "parse_Text" for a Text node, etc.) and then calls the methos.
        '''
        parseMethod = getattr(self, "parse_%s_" %node.__class__.__name__)
        parseMethod(node)
    def parse_Document(self, node):
        '''parse the document node
        The document node by itself isn't interesting (to us), but
        its only child, node, documentElement, is it's the root node
        of the grammar.
        '''
        self.parse(node.documentElement)
    def parse_Text(self, node):
        '''parse a text node
        The text of a text node is usually added to the output buffer
        verbatim. The noe exception is that <p class='sentence'> sets
        a flag to capitalize the first letter of the next word. If
        that flag is set, we capitalize the text and reset the flag.
        '''
        text = node.data
        if self.capitalizeNextWord:
            self.pieces.append(text[0].upper())
            self.pieces.append(text[1:])
            self.capitalizeNextWord = 0
        else:
            self.pieces.append(text)

    def parse_Element(self, node):
        '''parse an element
        An XML element corresponds to an actual tag in the source:
        <xref id='...'>, <p chance='...'>, <choice>, etc.
        Each element type is handled in its own method.  Like we did in
        parse(), we construct a method name based on the name of the
        element ("do_xref" for an <xref> tag, etc.) and
        call the method.
        '''
        handlerMethod = getattr(self, "do_%s" %node.tagName)
        handlerMethod(node)
    def parse_Comment(self, node):
        '''parse an comment'''
        pass
    def do_xref(self, node):
        '''do xref'''
        id = node.attributes["id"].value
        self.parse(self.randomChildElement(self.refs[id]))
    def do_p(self, node):
        '''do p'''
        keys = node.attributes.keys()
        if "class" in keys:
            if node.attributes["class"].value == "sentence":
                self.capitalizeNextWord = 1
        if "chance" in keys:
            chance = int(node.attributes["chance"].value)
            doit = (chance > random.randrange(100))
        else:
            doit = 1
        if doit:
            for child in node.childNodes:self.parse(child)

    def do_choice(self, node):
        '''do choice'''
        self.parse(self.randomChildElement(node))

def usage():
    print __doc__

def main(argv):
    grammar = "note.xml"
    for v in argv:
        print v
    try:
        opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt == '-d':
            _debug =1
        elif opt in ("-g", "--grammar"):
            grammar = arg
    source = "".join(args)
    k=KantGenerator(grammar, source)
    print k.output()

if __name__ == "__main__":
    main(sys.argv[1:])