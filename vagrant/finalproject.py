from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



#Fake Restaurants
restaurant = {'name': 'The Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'},
    {'name':'Blue Burgers', 'id':'2'},
    {'name':'Taco Hut', 'id':'3'},
    {'name':'Little Italy', 'id':'4'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


#Making an API Endpoint (GET Request)
# @app.route('/restaurant/<int:restaurant_id>/menu/JSON')
# def restaurantMenuJSON(restaurant_id):
#     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     items = session.query(MenuItem).filter_by(
#         restaurant_id=restaurant_id).all()
#     return jsonify(MenuItems=[i.serialize for i in items])
#
# @app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
# def menuItemJSON(restaurant_id, menu_id):
#     menuItem = session.query(MenuItem).filter_by(id=menu_id).one()
#     return jsonify(MenuItem=menuItem.serialize)
#
# ADD JSON API ENDPOINT HERE



@app.route('/')
@app.route('/restaurant/')
def showRestaurantMenu():
    return render_template('restaurants.html', restaurants = restaurants)

@app.route('/restaurant/new/')
def newRestaurant():
    return "new Restaurant"

@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET','POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = seccion.querry(restaurants).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editRestaurant.name = request.form['name']
        session.add(editRestaurant)
        session.commit
        #flash("new menu created!")
        return redirect(url_for('restaurantMenu',restaurants = restaurants_id))
    else:
        return render_template('editRestaurant.html', restaurant_ID = editedRestaurant)
    #return """This Page will be for editing restaurant %s" restaurant_id"""

@app.route('/restaurant/restaurant_id/delete/')
def deleteRestaurant():
    return """This Page will be for deleting restaurant %s" restaurant_id"""

@app.route('/restaurant/restaurant_id/')
@app.route('/restaurant/restaurant_id/menu')
def ShowMenu():
    return """This Page will the menu for restaurant %s" restaurant_id"""

@app.route('/restaurant/restaurant_id/menu/new/')
def newMenuItem():
    return """This Page is for making a new manu item for restaurant %s" restaurant_id"""

@app.route('/restaurant/restaurant_id/menu/menu_id/edit/')
def editMenuItem():
    return """This Page will be for editing menu item %s" menu_id"""

@app.route('/restaurant/restaurant_id/menu/menu_id/delete/')
def deleteMenuItem():
    return """This Page will be for deleting menu item %s" menu_id"""



#@app.route('/restaurant/new/', methods=['GET','POST'])
#def newMenuItem():
#    return "This Page will be for making a new restaurant"

#    if request.method == 'POST':
#        newItem = MenuItem(name = request.form['name'],restaurant_id = restaurant_id)
#        session.add(newItem)
#        session.commit()
#        flash("new menu created!")
#        return redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
#    else:
#        return render_template('newmenuitem.html',restaurant_id=restaurant_id)


# Task 2: Create route for editMenuItem function here

#@app.route('/restaurant/<int:restaurant_id><int:menu_id>/edit/', methods=['GET','POST'])
#def editMenuItem(restaurant_id, menu_id):
#    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
#    if request.method == 'POST':
#        if request.form['name']:
#            editedItem.name = request.form['name']
#        session.add(editedItem)
#        session.commit()
#        flash("Menu Modified!")
#        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
#    else:
#        # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
#        # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
#        return render_template(
#            'editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)
#
#
# Task 3: Create a route for deleteMenuItem function here
#
# @app.route('/restaurant/<int:restaurant_id><int:menu_id>/delete/', methods=['GET','POST'])
# def deleteMenuItem(restaurant_id, menu_id):
#     itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
#     if request.method == 'POST':
#         session.delete(itemToDelete)
#         session.commit()
#         flash("Item Deleted!")
#         return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
#     else:
#         # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
#         # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
#         return render_template(
#             'deletemenuitem.html', item=itemToDelete)


if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
