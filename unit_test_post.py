from app import app
import unittest

class TestPOSTCases(unittest.TestCase):
    def testAddProduct(self):
        tester = app.test_client(self)
        print("--- Test Save Product ---")
        p_rate = int(input("Product Rate  (int):"))
        p_name = input("Product Name (String: No need to write in quotes):")
        p_desc = input("Product Description (String: No need to write in quotes):")
        data = {"prodname":p_name,"prodrate":str(p_rate),"proddesc":str(p_desc)}
        resp = tester.post("/save-product",data=data,follow_redirects=True)
        status = resp.status_code
        self.assertEqual(status,200)

    def testUpdateProduct(self):
        tester = app.test_client(self)
        print("--- Test Update Product Details ---")
        p_code = int(input("Product Code (Int):"))
        p_rate = int(input("Product Rate (Int):"))
        p_name = input("Product Name :")
        p_desc = input("Product Description :")
        data = {"code":p_code,"name":p_name,"rate":str(p_rate),"desc":str(p_desc)}
        
        resp = tester.post("/update-product",data=data,follow_redirects=True)
        status = resp.status_code
        self.assertEqual(status,200)

if __name__ == "__main__":
    unittest.main()
