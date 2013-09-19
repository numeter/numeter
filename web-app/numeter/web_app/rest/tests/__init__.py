from wild_storage import Wild_Storage_Test


def suite():
    import unittest
    TEST_CASES = (
      'rest.tests.wild_storage',
    )
    suite = unittest.TestSuite()
    for t in TEST_CASES:
        suite.addTest(unittest.TestLoader().loadTestsFromModule(__import__(t, globals(), locals(), fromlist=["*"])))
    return suite
