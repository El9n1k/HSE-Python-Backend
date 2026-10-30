def select_products_by_category(products: list, category: str) -> list:
    answer = []
    for product in products:
        if product.category == category:
            answer.append(product)
    return answer
