class univariate():
    def quanqual(dataset):
        quan = dataset.select_dtypes(include=["number"]).columns.tolist()
        qual = dataset.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
        return quan, qual
    
    # quan,qual =quanqual(dataset)
    # print("Quantitative:", quan)
    # print("Qualitative:", qual)
