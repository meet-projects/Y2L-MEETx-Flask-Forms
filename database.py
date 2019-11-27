from model import Base, Product, Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(input_name, input_price, input_picture, input_description):
    """
    Add a product to the database, given
    their name, 
    """
    product_object = Product(
        name=input_name,
        price=input_price,
        picture=input_picture,
        description = input_description)
    session.add(product_object)
    session.commit()




def query_all():
   """
   Get all the products
   in the database.
   """
   products = session.query(
      Product).all()
   return products


for prod in query_all():
	print(prod.name,prod.price,prod.id)

def query_by_id(prod_id):
   """
   Find the first product
   in the database, by its id
   """
   product = session.query(
       Product).filter_by(
       id=prod_id).first()
   return product

def update_price (prod_id, price):
   """
   Update a product in the database, with price
   """
   product = session.query(
       Product).filter_by(
       id=prod_id).first()
   product.price = price
   session.commit()


#update_lab_status(0, 250.00)


def delete_product(prod_id):
   """
   Delete product with certain id
   """
   session.query(Product).filter_by(
       id=prod_id).delete()
   session.commit()

def add_to_cart(prod_id):
    """
    Add a product to the cart
    """
    cart_object = Cart(
        product_id=prod_id)
    session.add(cart_object)
    session.commit()