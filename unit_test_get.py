from app import app
import unittest

class TestGETCases(unittest.TestCase):
    print("--- Testing only API response 200 ok ---")
    print("Note : Please Enter Proper deatils with correct datatypes to run this API's ")
    print("--")
    def testHomePage(self):
        print("--- Test Home Page ---")
        tester = app.test_client(self)
        resp = tester.get("/")
        status = resp.status_code
        self.assertEqual(status,200)

    def testHomePage(self):
        print("--- Test Add Product Page ---")
        tester = app.test_client(self)
        resp = tester.get("/new-product")
        status = resp.status_code
        self.assertEqual(status,200)

    def testGetProductDetails(self):
        tester = app.test_client(self)
        print("--- Test Get Single Product Details ---")
        code = int(input("Enter Product Code (Int):"))
        resp = tester.get("/product-details/"+str(code))
        status = resp.status_code
        self.assertEqual(status,200)

if __name__ == "__main__":
    unittest.main()