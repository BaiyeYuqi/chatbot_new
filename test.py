# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 17:39:24 2019

@author: whq672437089
"""

import unittest 
import preprocess as pp

class testPreprocess(unittest.TestCase):
    def setUp(self):
        self.content="- - what is the illuminati \n - secret - - what is vineland \n - novel"
        self.template={"what is the illuminati":" secret","what is vineland":" novel"}
        self.question="what is  illuminati .\n what is vineland .\n "
    
    def tearDown(self):
        del self.content
        del self.template
    
    def testGenerateConversationTurnDict(self):
        self.assertTrue(self.template==pp.generateConversationTurnDict(self.content))
        
    def testPureQuestionText(self):
        self.assertTrue(self.question==pp.pureQuestionsText(self.template))
        
def mySuite():
    suite=unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testPreprocess))
    return suite

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(mySuite())