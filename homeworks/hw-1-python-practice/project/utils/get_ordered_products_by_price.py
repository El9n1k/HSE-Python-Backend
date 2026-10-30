def get_ordered_products_by_price(products: list) -> list:
    answer = []
    for product in products:
        answer.append(product)
    answer.sort(key=lambda product: -product.price)
    return answer
