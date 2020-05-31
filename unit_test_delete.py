from app import app
import unittest

class TestDELETECase(unittest.TestCase):
    print("--- Testing only API response 200 ok ---")
    print("Note : Please Enter Proper deatils with correct datatypes to run this API's ")
    print("--")
    def testDeleteProduct(self):
        tester = app.test_client(self)
        print("--- Test Delete Single Product ---")
        code = int(input("Enter Product Code (Int):"))
        resp = tester.get("/delete-product/"+str(code))
        status = resp.status_code
        self.assertEqual(status,200)

if __name__ == "__main__":
    unittest.main()