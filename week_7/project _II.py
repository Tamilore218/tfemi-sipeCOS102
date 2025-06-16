import pandas as pd

data = {
    "Segment": [
        "Refreshment Beverages", "Refreshment Beverages",
        "Confectionery", "Confectionery", "Confectionery",
        "Intermediate Cocoa Products", "Intermediate Cocoa Products",
        "Intermediate Cocoa Products", "Intermediate Cocoa Products"
    ],
    "Brand": [
        "CADBURY BOURNVITA", "CADBURY 3-in-1 HOT CHOCOLATE",
        "TOMTOM CLASSIC", "TOMTOM STRAWBERRY", "BUTTERMINT",
        "COCOA POWDER", "COCOA BUTTER", "COCOA LIQUOR", "COCOA CAKE"
    ],
    "Export/Local": [
        "Local", "Local",
        "Local", "Local", "Local",
        "Local", "Export", "Export", "Export"
    ]
}

df = pd.DataFrame(data)
df.to_csv("cadbury_market.csv", index=False)
print("CSV file created!")
