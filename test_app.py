import unittest
import os

# create an in-memory database to be tested
os.environ["DATABASE_URL"] = "sqlite://"

from main import app, db


class TestCase(unittest.TestCase):
    def setUp(self):
        # set up
        self.app = app
        # set up app context to allow access outside of
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()
        # create empty tables for the models defined in the app
        db.create_all()

    def tearDown(self):
        # reset after test
        # drop all tables from in-memory db
        db.drop_all()
        self.app_ctxt.pop()
        self.app = None
        self.app_ctxt = None

    def test_app(self):
        # test that app has been initialised
        assert self.app is not None
        assert app == self.app


if __name__ == "__main__":
    unittest.main()
