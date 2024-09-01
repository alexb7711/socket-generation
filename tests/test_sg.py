#!/usr/bin/python

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Standard Lib
import SIG.sig as sig
import os
import unittest

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Packages

# ===============================================================================
#


class TestSIG(unittest.TestCase):
    # -------------------------------------------------------------------------------
    #
    def get_files():
        d = sig.SIG("./examples", "./examples/build")
        d.run()
        return d

    # -------------------------------------------------------------------------------
    #
    def test_dir_search(self):
        # Find the files
        d = TestSIG.get_files()
        f = d.get_files()

        # Count the files
        self.assertEqual(len(f), 1)

        # Check file names
        pwd = os.path.abspath("./examples")

        self.assertEqual(pwd + "/topics/topic_position.yml", f[0])

        return

    # -------------------------------------------------------------------------------
    #
    def test_first_level_data_structure(self):
        # Find the files
        d = TestSIG.get_files()
        f = d.get_data()

        # Topics
        self.assertEqual(f[0].name, "test_topic")
        self.assertEqual(f[0].lang, ["python"])
        self.assertEqual(f[0].protocol, "UDP")
        self.assertTrue(isinstance(f[0].data["int"], list))
        self.assertEqual(f[0].desc, "This is a test topic")

        return
