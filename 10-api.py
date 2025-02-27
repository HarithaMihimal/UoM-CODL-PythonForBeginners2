import requests
BASE_URL= "http://host1.open.uom.lk"

product={
        "productName":"Araliya Basmathi Rice",
        "description":"White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
        "category":"Rice",
        "brand":"CIC",
        "expiredDate":"2023.05.04",
        "manufacturedDate":"2022.02.20",
        "batchNumber":324567,
        "unitPrice":1020,
        "quantity":200,
        "createdDate":"2022.02.24"
}
response=requests.post(f"{BASE_URL}/api/products",json=product)
print(response.status_code)
